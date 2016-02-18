class Description(object):
    """Implements <dl> tag"""


    def __init__(self, text=None, horizontal=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.horizontal = horizontal

        if text:
            self.children.append(text)

    def __str__(self):
        output = [ "<dl" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl or self.horizontal:
            output.append(" class=\"")
            if self.horizontal:
                output.append("dl-horizontal")
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

        output.append("</dl>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
