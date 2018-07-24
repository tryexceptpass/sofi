from .element import Element


class Button(Element):
    """Implements the <button> tag"""

    SEVERITIES = {
        'danger': 'btn-danger',
        'success': 'btn-success',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'primary': 'btn-primary',
        'secondary': 'btn-secondary',
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
        if severity is not None and severity not in Button.SEVERITIES:
            raise ValueError(f"Unknown severity: {severity}")

        if size is not None and size not in Button.SIZES:
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
            if self.outline:
                classes.append(Button.SEVERITIES[self.severity].replace('btn-', 'btn-outline-'))
            else:
                classes.append(Button.SEVERITIES[self.severity])

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


class ButtonGroup(Element):
    """Implements a button group <div class=\"btn-group\">"""

    SIZES = {
        'large': 'btn-group-lg',
        'lg': 'btn-group-lg',
        'small': 'btn-group-sm',
        'sm': 'btn-group-sm',
    }

    def __init__(self, size=None, vertical=False, label=None, cl=None, ident=None, style=None, attrs=None):
        if size is not None and size not in ButtonGroup.SIZES:
            raise ValueError(f'Unknown size: {size}')

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.vertical = vertical
        self.label = label

    def __repr__(self):
        return f'<ButtonGroup(size="{self.size}")>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        classes = ["btn-group"]

        if self.cl:
            classes.append(self.cl)

        if self.vertical:
            classes.append("btn-group-vertical")

        if self.size:
            classes.append(ButtonGroup.SIZES[self.size])

        output.append(f'class="{" ".join(classes)}" role="group"')

        if self.label:
            output.append(f' aria-label="{self.label}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)


class ButtonToolbar(Element):
    """Implements a button toolbar <div class=\"btn-toolbar\">"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<ButtonToolbar()>"

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="btn-toolbar')

        if self.cl:
            output.append(f' {self.cl}')

        output.append('" role="toolbar"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)
