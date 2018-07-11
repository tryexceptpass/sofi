from .element import Element
from .column import Column


class Row(Element):
    """Implements row layout with format <div class=\"row\">"""

    ALIGNMENT = {
        'start': 'justify-content-start',
        'center': 'justify-content-center',
        'end': 'justify-content-end'
        'around': 'justify-content-around'
        'between': 'justify-content-between'
    }
    VERTICAL_ALIGNMENT = {'start': 'align-items-start', 'center': 'align-items-center', 'end': 'align-items-end'}

    def __init__(self, align=None, valign=None, cl=None, ident=None, style=None, attrs=None):
        if align is not None and valign not in Row.ALIGNMENT:
            raise ValueError(f"Unknown alignment: {align}")

        if valign is not None and valign not in Row.VERTICAL_ALIGNMENT:
            raise ValueError(f"Unknown vertical alignment: {valign}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.align = align
        self.valign = valign


    def newcolumn(self, item, **kwargs):
        c = Column(**kwargs)
        c.addelement(item)
        self.addelement(c)

        return c

    def __repr__(self):
        return f'<Row(valign="{self.valign}")>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="row')

        if self.align:
            output.append(f' {Row.ALIGNMENT[self.align]}')

        if self.valign:
            output.append(f' {Row.VERTICAL_ALIGNMENT[self.valign]}')

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)
