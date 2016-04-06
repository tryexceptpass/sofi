from .element import Element

class TableFoot(Element):
    """Implements the <tfoot> tag"""

    def __init__(self, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

    def __str__(self):
        output = [ "<tfoot" ]

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

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</tfoot>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
