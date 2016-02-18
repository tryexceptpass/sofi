class UnorderedList(object):
    """Implements <ul> tag"""


    def __init__(self, text=None, unstyled=False, inline=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.unstyled = unstyled
        self.inline = inline

        if text:
            self.children.append(text)

    def __str__(self):
        output = [ "<ul" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl or self.unstyled or self.inline:
            output.append(" class=\"")
            if self.unstyled:
                output.append("list-unstyled")
                if self.cl:
                    output.append(" ")
            elif self.inline:
                output.append("list-inline")
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

        output.append("</ul>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
