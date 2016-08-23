from .element import Element

class Badge(Element):
    """Implement Badges"""

    def __init__(self, text=None, ident=None, style=None, attrs=None):
        super().__init__(ident=ident, style=style, attrs=attrs)

        if text:
            self.children.append(text)

    def __repr__(self):
        return "<Span class=\"badge\">"

    def __str__(self):
        output = [ "<span" ]

        output.append(" class=\"badge\"")

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")
        
        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</span>")

        return "".join(output)
