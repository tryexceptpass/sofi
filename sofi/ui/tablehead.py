from .element import Element
from .tablerow import TableRow
from .tablecell import TableCell

class TableHead(Element):
    """Implements the <thead> tag"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def addrow(self, *args, **kwargs):
        tr = TableRow(**kwargs)

        for item in args:
            if isinstance(item, Element):
                tr.addelement(item)
            else:
                tr.addelement(TableCell(item, head=True))


        self.addelement(tr)

        return tr

    def __repr__(self):
        return "<TableHead>"

    def __str__(self):
        output = [ "<thead" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
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

        output.append("</thead>")

        return "".join(output)
