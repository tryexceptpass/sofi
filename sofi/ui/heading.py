from .element import Element

class Heading(Element):
    """Implements heading tags using size attribute: <h1>, <h2>, etc."""

    def __init__(self, size=1, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Heading(size=" + str(self.size) + ")>"

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

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</h")
        output.append(str(self.size))
        output.append(">")

        return "".join(output)
