from .element import Element

class Button(Element):
    """Implements the <button> tag"""

    STYLES = { 'danger':  'btn-danger',
               'success': 'btn-success',
               'info':    'btn-info',
               'warning': 'btn-warning',
               'primary': 'btn-primary',
               'default': 'btn-default'
             }

    def __init__(self, text=None, buttontype=None, href="#", cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

        self.text = text
        self.buttontype = buttontype

    def __repr__(self):
        return "<Button(text='" + self.text + "')>"

    def __str__(self):
        output = [ "<button" ]

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        output.append(' class=\"btn ')
        if self.buttontype:
            output.append(Button.STYLES[self.buttontype])
        else:
            output.append(Button.STYLES['default'])
        if self.cl:
            output.append(' ')
            output.append(self.cl)
        output.append('"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        output.append('>')
        output.append(self.text)

        for child in self.children:
            output.append(str(child))

        output.append("</button>")

        return "".join(output)
