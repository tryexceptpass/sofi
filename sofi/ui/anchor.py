from .element import Element

class Anchor(Element):
    """Implements the <a> tag"""


    def __init__(self, text=None, href="#", cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.href = href

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Anchor(href='" + self.href + "')>"

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

        output.append(' href="')
        output.append(self.href)
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

        output.append("</a>")

        return "".join(output)
