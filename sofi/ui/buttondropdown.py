from .element import Element
from .button import Button
from .buttongroup import ButtonGroup
from .dropdownitem import DropdownItem
from .unorderedlist import UnorderedList

class ButtonDropdown(Element):
    """Implements a button dropdown <div class=\"btn-toolbar\">"""

    def __init__(self, text=None, split=False, severity=None, dropup=False, size=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.split = split
        self.severity = severity
        self.dropup = dropup
        self.size = size

    def __repr__(self):
        return "<ButtonDropdown(text='" + self.text + "',split=" + self.split + ")>"

    def __str__(self):
        grpid = None
        if self.ident:
            grpid = self.ident + "-button-dropdown"

        classes = None
        if self.dropup:
            classes = "dropup"

        grp = ButtonGroup(cl=classes, ident=grpid, style=self.style, attrs=self.attrs)

        classes = []
        if not self.split:
            classes.append("dropdown-toggle")

        if self.cl:
            classes.append(self.cl)

        btntxt = ""
        if self.text:
            btntxt = self.text

        btnattrs = None
        if not self.split:
            btnattrs = { 'data-toggle': 'dropdown' }
            btntxt += ' <span class="caret"></span>'

        btn = Button(text=btntxt, severity=self.severity, size=self.size, cl=" ".join(classes), ident=self.ident, style=self.style, attrs=btnattrs)
        grp.addelement(btn)

        if self.split:
            classes.append("dropdown-toggle")
            splitbtn = Button(text='<span class="caret"></span>', severity=self.severity, size=self.size, cl=" ".join(classes), attrs={'data-toggle':'dropdown'})
            grp.addelement(splitbtn)

        ul = UnorderedList(cl="dropdown-menu")
        grp.addelement(ul)

        for child in self._children:
            if type(child) == DropdownItem:
                ul.addelement(child)
            else:
                grp.addelement(child)

        return str(grp)
