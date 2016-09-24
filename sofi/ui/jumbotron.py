from .element import Element

class Jumbotron(Element):
    """Implements the Bootstrap Jumbotron <div class="jumbotron">"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Jumbotron>"

    def __str__(self):
        output = [ "<div" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        classes = []
        classes.append("jumbotron")

        if self.cl:
            classes.append(self.cl)

        output.append(' class="')
        output.append(" ".join(classes))
        output.append('"')

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

        output.append("</div>")

        return "".join(output)