from .element import Element

class Form(Element):
    """Implements the <form> tag"""

    def __init__(self, inline=False, horizontal=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.inline = inline
        self.horizontal = horizontal

    def __str__(self):
        output = [ "<form" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        cls = []
        if self.inline:
            cls.append('form-inline')

        if self.horizontal:
            cls.append('form-horizontal')

        if self.cl:
            cls.append(self.cl)

        if len(cls) > 0:
            output.append(" class=\"")
            output.append(" ".join(cls))
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</form>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
