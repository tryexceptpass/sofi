from .element import Element

class Blockquote(Element):
    """Implements the <blockquote> tag"""

    def __init__(self, text=None, reverse=False, cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

        self.reverse = reverse

        if text:
            self.children.append(text)

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

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</blockquote>")

        return "".join(output)
