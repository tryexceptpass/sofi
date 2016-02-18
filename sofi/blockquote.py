class Blockquote(object):
    """Implements the <blockquote> tag"""

    def __init__(self, text=None, reverse=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.reverse = reverse

        if text:
            self.children.append(text)

    def __str__(self):
        output = [ "<blockquote" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl or self.reverse:
            output.append(" class=\"")
            if self.reverse:
                output.append("blockquote-reverse")
                if self.cl:
                    output.append(" ")
            if self.cl:
                output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</blockquote>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
