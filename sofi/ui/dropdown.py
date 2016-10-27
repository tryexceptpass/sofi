from .element import Element
from .listitem import ListItem
from .button import Button
from .div import Div
from .anchor import Anchor
from .span import CaretSpan
from .unorderedlist import UnorderedList

from collections import OrderedDict

class Dropdown(Element):
    """Implements a Bootstrap dropdown tag"""

    def __init__(self, text, dropup=False, align='left', navbaritem=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.dropup = dropup
        self.align = align
        self.navbaritem = navbaritem

    def __repr__(self):
        return '<Dropdown(text="' + self.text + ',dropup=' + str(self.dropup) + ')>'

    def __str__(self):
        output = []

        ident = None
        if self.ident:
            ident = self.ident + "-dropdown"

        cl = "dropup" if self.dropup else "dropdown"

        if self.cl:
            cl += " " + self.cl

        btn = None
        if self.navbaritem:
            btn = ListItem(cl=cl, ident=ident, style=self.style, attrs=self.attrs)

            attrs = OrderedDict()
            attrs["role"] = "button"
            attrs["data-toggle"] = "dropdown"
            attrs["aria-haspopup"] = "true"
            attrs["aria-expanded"] = "false"

            a = Anchor(self.text + " ", cl="dropdown-toggle", ident=self.ident, attrs=attrs)
            a.addelement(CaretSpan())
            btn.addelement(a)
        else:
            btn = Div(cl=cl, ident=ident, style=self.style, attrs=self.attrs)
            b = Button(self.text + " ", cl="dropdown-toggle", ident=self.ident, attrs={"data-toggle": "dropdown"})
            b.addelement(CaretSpan())
            btn.addelement(b)


        output.append(str(btn))

        cl = "dropdown-menu"
        if self.align == 'right':
            cl = cl + " dropdown-menu-right"

        ul = UnorderedList(cl=cl)

        for child in self._children:
            ul.addelement(child)

        btn.addelement(ul)

        return str(btn)
