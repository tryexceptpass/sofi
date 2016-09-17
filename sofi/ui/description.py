from .element import Element

class Description(Element):
    """Implements <dl> tag"""


    def __init__(self, text=None, horizontal=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.horizontal = horizontal

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Description(horizontal=" + self.horizontal + ")>"

    def __str__(self):
        output = [ "<dl" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl or self.horizontal:
            output.append(" class=\"")
            if self.horizontal:
                output.append("dl-horizontal")
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

        output.append("</dl>")

        return "".join(output)
