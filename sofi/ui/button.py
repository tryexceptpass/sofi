from .element import Element

class Button(Element):
    """Implements the <button> tag"""

    SEVERITIES = { 'danger':  'btn-danger',
                   'success': 'btn-success',
                   'info':    'btn-info',
                   'warning': 'btn-warning',
                   'primary': 'btn-primary',
                   'default': 'btn-default'
                 }

    def __init__(self, text=None, severity=None, size=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.size = size

    def __repr__(self):
        return "<Button(text='" + self.text + "')>"

    def __str__(self):
        output = [ "<button" ]

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        classes = [ "btn" ]
        output.append(' class="')
        if self.severity:
            classes.append(Button.SEVERITIES[self.severity])
        else:
            classes.append(Button.SEVERITIES['default'])
        if self.size:
            if self.size == "large" or self.size == "lg":
                classes.append("btn-lg")
            elif self.size == "small" or self.size == "sm":
                classes.append("btn-sm")
            elif self.size == "xsmall" or self.size == "xs":
                classes.append("btn-xs")
        if self.cl:
            classes.append(self.cl)
        output.append(" ".join(classes))
        output.append('" type="button"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append('>')

        if self.text:
            output.append(self.text)

        for child in self._children:
            output.append(str(child))

        output.append("</button>")

        return "".join(output)
