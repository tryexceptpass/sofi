class Abbreviation(object):
    """Implementation of the <abbr> tag"""

    def __init__(self, title="", text=None, initialism=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.title = title
        self.initialism = initialism

        if text:
            self.children.append(text)

    def __str__(self):
        output = [ "<abbr title=\"", self.title, "\"" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl or self.initialism:
            output.append(" class=\"")
            if self.initialism:
                output.append("initialism")
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

        output.append("</abbr>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
