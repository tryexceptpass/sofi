from .element import Element


class Column(Element):
    """Implements the column layout <div class=\"col-\"> where size, count and offset
    attributes are used to create the class name, i.e.: col-md-4 or col-offset-md-4"""

    VERTICAL_ALIGNMENT = {'start': 'align-items-start', 'center': 'align-items-center', 'end': 'align-items-end'}

    def __init__(self, size='md', count=4, offset=0, valign=None, order=None, cl=None, ident=None, style=None, attrs=None):
        if valign is not None and valign not in Column.VERTICAL_ALIGNMENT:
            raise ValueError(f"Unknown vertical alignment: {valign}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.count = count
        self.offset = offset
        self.valign = valign
        self.order = order

    def __repr__(self):
        return f'<Column(size={self.size},count={self.count},offset={self.offset})>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append(f'class="col-{self.size}-{self.count}')

        if self.offset > 0:
            output.append(f' col-{self.size}-offset-{self.offset}')

        if self.cl:
            output.append(f" {self.cl}")

        if self.order:
            output.append(f' order-{self.order}')

        if self.valign:
            output.append(f' {Column.VERTICAL_ALIGNMENT[self.valign]}')

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)
