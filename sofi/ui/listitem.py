from .element import Element

class ListItem(Element):
    """Implements <li> tag"""


    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text

    def __repr__(self):
        return "<ListItem>"

    def __str__(self):
        output = [ "<li" ]

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

        if self.text:
            output.append(self.text)

        for child in self._children:
            output.append(str(child))

        output.append("</li>")

        return "".join(output)
