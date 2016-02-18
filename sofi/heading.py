class Heading(object):
    """Implements heading tags using size attribute: <h1>, <h2>, etc."""

    def __init__(self, size=1, text=None, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.size = size

        if text:
            self.children.append(text)

    def __str__(self):
        output = [ "<h", str(self.size) ]

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

        output.append("</h")
        output.append(str(self.size))
        output.append(">")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
