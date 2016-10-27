from .element import Element
from .anchor import Anchor

class DropdownItem(Element):
    """Implements an item from a Dropdown list"""

    def __init__(self, text=None, disabled=False, header=False, divider=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.disabled = disabled
        self.header = header
        self.divider = divider

    def __repr__(self):
        return '<DropdownItem(text="' + self.text + '",disabled=' + self.disabled + ',header=' + self.header + ',divider=' + self.divider + ')>'

    def __str__(self):
        output = [ '<li' ]

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        cls = []

        if self.header:
            cls.append("dropdown-header")
        elif self.divider:
            cls.append("divider")
        elif self.disabled:
            cls.append("disabled")
            
        if self.cl:
            cls.append(self.cl)

        if len(cls) > 0:
            output.append(' class="')
            output.append(' '.join(cls))
            output.append('"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append('>')

        if self.text:
            output.append(str(Anchor(self.text)))

        for child in self._children:
            output.append(str(child))

        output.append('</li>')

        return "".join(output)
