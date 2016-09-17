from .element import Element

class Span(Element):
    """Implements <span> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Span>"

    def __str__(self):
        output = [ "<span" ]

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

        output.append("</span>")

        return "".join(output)

class CaretSpan(Span):
    """Implements a span that contains a caret icon, useful in dropdowns and other similar situations"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        if cl:
            cl = cl + " caret"
        else:
            cl = "caret"

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)
