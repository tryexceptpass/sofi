from .element import Element

class Alert(Element):
    """Implements the <div class="alert"> tag"""

    SEVERITIES = { 'danger':  'alert-danger',
                   'success': 'alert-success',
                   'info':    'alert-info',
                   'warning': 'alert-warning'
                 }

    def __init__(self, text=None, severity=None, closebtn=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.closebtn = closebtn

    def __repr__(self):
        return "<Alert(text='" + self.text + "')>"

    def __str__(self):
        output = [ "<div" ]

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        classes = [ "alert" ]
        output.append(' class="')

        if self.severity:
            classes.append(Alert.SEVERITIES[self.severity])
        if self.closebtn:
            classes.append("alert-dismissible fade in")
        if self.cl:
            classes.append(self.cl)

        output.append(" ".join(classes))
        output.append('"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(' role="alert"')
        output.append('>')

        if self.closebtn:
            output.append('<button type="button" class="close"')
            output.append(' data-dismiss="alert" aria-label="Close">')
            output.append('<span aria-hidden="true">&times;</span>')
            output.append('</button>')

        if self.text:
            output.append(self.text)

        for child in self._children:
            output.append(str(child))

        output.append("</div>")

        return "".join(output)
