from .element import Element
from .button import Button


class ButtonGroup(Element):
    """Implements a button group <div class=\"btn-group\">"""

    SIZES = {
        'large': 'btn-group-lg',
        'lg': 'btn-group-lg',
        'small': 'btn-group-sm',
        'sm': 'btn-group-sm',
    }

    def __init__(self, size=None, vertical=False, label=None, cl=None, ident=None, style=None, attrs=None):
        if size is not None and size is not in ButtonGroup.SIZES:
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
