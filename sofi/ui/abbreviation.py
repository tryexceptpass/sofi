from .element import Element

class Abbreviation(Element):
    """Implementation of the <abbr> tag"""

    def __init__(self, title="", text=None, initialism=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.title = title
        self.initialism = initialism

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Abbreviation(title='" + self.title + "',initialism=" + str(self.initialism) + ")>"

    def __str__(self):
        output = [ "<abbr title=\"", self.title, "\"" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl or self.initialism:
            output.append(" class=\"")
            if self.initialism:
                output.append("initialism")
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

        output.append("</abbr>")

        return "".join(output)
