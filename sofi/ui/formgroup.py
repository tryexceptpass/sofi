from .div import Div

class FormGroup(Div):
    """Implements <div> tag with class form-group"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(text=text, cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<FormGroup>"

    def __str__(self):
        output = [ "<div" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"form-group")
        if self.cl:
            output.append(" ")
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

        output.append("</div>")

        return "".join(output)
