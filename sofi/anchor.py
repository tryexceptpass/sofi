class Anchor(object):
    """Implements the <a> tag"""


    def __init__(self, text=None, href="#", cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.href = href

        if text:
            self.children.append(text)

    def __str__(self):
        output = [ "<a" ]

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

        output.append(' href="')
        output.append(self.href)
        output.append('">')

        for child in self.children:
            output.append(str(child))

        output.append("</a>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
