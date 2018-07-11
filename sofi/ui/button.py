from .element import Element

class Button(Element):
    """Implements the <button> tag"""

    SEVERITIES = {
        'danger':  'btn-danger',
        'success': 'btn-success',
        'info':    'btn-info',
        'warning': 'btn-warning',
        'primary': 'btn-primary',
        'secondary': 'btn-secondary'
        'light': 'btn-light',
        'dark': 'btn-dark',
        'link': 'btn-link'
    }

    SIZES = {
        'large': 'btn-lg',
        'ld': 'btn-lg',
        'small': 'btn-sm',
        'sm': 'btn-sm'
    }

    def __init__(self, text=None, severity=None, size=None, outline=False, block=False, cl=None, ident=None, style=None, attrs=None):
        if severity is not None and not in Button.SEVERITIES:
            raise ValueError(f"Unknown severity: {severity}")

        if size is not None and not in Button.SIZES:
            raise ValueError(f"Unknown size: {size}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.size = size
        self.outline = outline
        self.block = block

    def __repr__(self):
        return f'<Button(text="{self.text}")>'

    def __str__(self):
        output = ["<button"]

        if self.ident:
            output.append(f' id="{self.ident}" ')

        classes = ["btn"]

        if self.severity:
            if outline:
                classes.append(Button.SEVERITIES[self.severity].replace('btn-', 'btn-outline-'))
            else:
                classes.append(Button.SEVERITIES[self.severity])

        else:
            classes.append(Button.SEVERITIES['default'])

        if self.size:
            classes.append(Button.SIZES[self.size])

        if self.block:
            classes.append('btn-block')
        if self.cl:
            classes.append(self.cl)

        output.append(f' class="{" ".join(classes)}" type="button"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append('>')

        if self.text:
            output.append(self.text)

        output.extend([str(child) for child in self._children])

        output.append("</button>")

        return "".join(output)
