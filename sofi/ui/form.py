from .element import Element

class Form(Element):
    """Implements the <form> tag"""

    def __init__(self, inline=False, horizontal=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.inline = inline
        self.horizontal = horizontal

    def __repr__(self):
        return "<Form(inline=" + self.inline + ",horizontal=" + self.horizontal + ")>"

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

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</form>")

        return "".join(output)
