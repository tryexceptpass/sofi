from .element import Element
from .anchor import Anchor

class NavbarItem(Element):
    """Implements an item for a Navbar"""

    def __init__(self, text='', href=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.href = href

    def __repr__(self):
        if self.href is None:
            return '<NavbarItem(text="' + self.text + '")>'
        else:
            return '<NavbarItem(text="' + self.text + '",href=' + self.href + ')>'

    def __str__(self):
        output = []

        if self.href is None:
            output.append('<p')

        else:
            output.append('<li')

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        cls = []
        if self.href is None:
            cls.append('navbar-text')

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

        if self.href is None:
            output.append(self.text)
        else:
            output.append(str(Anchor(self.text, self.href)))

        for child in self._children:
            output.append(str(child))

        if self.href is None:
            output.append("</p>")
        else:
            output.append('</li>')

        return "".join(output)
