class Row(object):
    """Implements row layout with format <div class=\"row\">"""

    def __init__(self, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

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

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</div>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
