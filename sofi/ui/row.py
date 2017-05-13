from .element import Element
from .column import Column

class Row(Element):
    """Implements row layout with format <div class=\"row\">"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def newcolumn(self, item, **kwargs):
        c = Column(**kwargs)
        c.addelement(item)
        self.addelement(c)

        return c

    def __repr__(self):
        return "<Row>"

    def __str__(self):
        output = [ "<div " ]

        if self.ident:
            output.append("id=\"")
            output.append(self.ident)
            output.append("\" ")

        output.append("class=\"row")

        if self.cl:
            output.append(" ")
            output.append(self.cl)

        output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</div>")

        return "".join(output)
