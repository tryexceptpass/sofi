from .element import Element
from .anchor import Anchor
from .text import Heading


class Alert(Element):
    """Implements the <div class="alert"> tag."""

    SEVERITIES = {
        'danger': 'alert-danger',
        'success': 'alert-success',
        'info': 'alert-info',
        'warning': 'alert-warning',
        'light': 'alert-light',
        'dark': 'alert-dark',
        'primary': 'alert-primary',
        'secondary': 'alert-secondary'
    }

    def __init__(self, text=None, severity=None, closebtn=False, cl=None, ident=None, style=None, attrs=None):
        if severity is not None and severity not in Alert.SEVERITIES:
            raise ValueError(f"Unknown severity: {severity}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.closebtn = closebtn

    def __repr__(self):
        return f'<Alert(text="{self.text}")>'

    def __str__(self):
        output = ["<div"]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        classes = ["alert"]

        if self.severity:
            classes.append(Alert.SEVERITIES[self.severity])
        if self.closebtn:
            classes.append("alert-dismissible fade in")
        if self.cl:
            classes.append(self.cl)

        output.append(f' class="{" ".join(classes)}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(' role="alert">')

        if self.closebtn:
            output.append(
                '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
                '<span aria-hidden="true">&times;</span>'
                '</button>'
            )

        if self.text:
            output.append(self.text)

        for child in self._children:
            if isinstance(child, Anchor) and 'alert-link' not in child.cl:
                child.cl += "alert-link" if len(child.cl) == 0 else " alert-link"

            elif isinstance(child, Heading):
                child.cl += "alert-heading" if len(child.cl) == 0 else " alert-heading"

            output.append(str(child))

        output.append("</div>")

        return "".join(output)
