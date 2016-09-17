from .element import Element

class Blockquote(Element):
    """Implements the <blockquote> tag"""

    def __init__(self, text=None, reverse=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.reverse = reverse

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Blockquote(reverse=" + str(self.reverse) + ")>"

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

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</blockquote>")

        return "".join(output)
