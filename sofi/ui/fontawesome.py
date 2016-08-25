from .element import Element

class FontAwesomeIcon(Element):
    """Implements Font Awesome Icons"""

    def __init__(self, icon=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.icon = icon

    def __repr__(self):
        return "<FontAwesomeIcon(icon='" + self.icon + "')>"

    def __str__(self):
        output = [ "<i" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        classes = ["fa"]

        if self.icon:
            classes.append("fa-"+self.icon)

        if self.cl:            
            classes.append(self.cl)
            
        output.append(" class=\"")
        output.append(" ".join(classes))
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

        output.append("</i>")

        return "".join(output)
