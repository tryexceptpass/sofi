from .element import Element

class UnorderedList(Element):
    """Implements <ul> tag"""


    def __init__(self, text=None, unstyled=False, inline=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.unstyled = unstyled
        self.inline = inline

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<UnorderedList(unstyled=" + str(self.unstyled) + ",inline=" + str(self.inline) + ")>"

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

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</ul>")

        return "".join(output)
