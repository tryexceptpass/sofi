from .element import Element

class ButtonToolbar(Element):
    """Implements a button toolbar <div class=\"btn-toolbar\">"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<ButtonToolbar()>"

    def __str__(self):
        output = [ "<div " ]

        if self.ident:
            output.append('id="')
            output.append(self.ident)
            output.append('" ')

        output.append('class="btn-toolbar')

        if self.cl:
            output.append(" ")
            output.append(self.cl)

        output.append('" role="toolbar"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</div>")

        return "".join(output)
