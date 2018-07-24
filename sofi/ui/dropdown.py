import secrets

from .element import Element
from .lists import ListItem
from .button import Button, ButtonGroup
from .div import Div
from .anchor import Anchor


class Dropdown(Element):
    """Implements a Bootstrap dropdown <div class="dropdown"> component"""

    DIRECTIONS = {
        'up': 'dropup',
        'left': 'dropleft',
        'right': 'dropright',
        'down': 'dropdown'
    }

    def __init__(self, text, severity=None, dropdirection='down', split=False, align='left', size=None, asnavitem=False,
                 asbtngrp=False, offset=None, reference=None, cl=None, ident=None, style=None, attrs=None):
        if dropdirection is not None and dropdirection not in Dropdown.DIRECTIONS:
            raise ValueError(f"Unknown direction: {dropdirection}")

        if size is not None and size not in Button.SIZES:
            raise ValueError(f"Unknown size: {size}")

        if align not in ('left', 'right'):
            raise ValueError(f"Unknown alignment: {align}")

        super().__init__(cl=cl, ident=secrets.token_hex(8) if ident is None else ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.dropdirection = dropdirection
        self.split = split
        self.align = align
        self.size = size
        self.asnavitem = asnavitem
        self.asbtngrp = asbtngrp
        self.offset = offset
        self.reference = reference

    def __repr__(self):
        return f'<Dropdown(text="{self.text}",severity={self.severity},split={self.split},direction="{self.dropdirection}")>'

    def __str__(self):

        wrappercl = [Dropdown.DIRECTIONS[self.dropdirection]]

        if self.cl:
            wrappercl.append(self.cl)

        btnattrs = {'data-toggle': 'dropdown', 'aria-haspopup': 'true', 'aria-expanded': 'false'}

        if self.offset:
            btnattrs['data-offset'] = self.offset

        if self.reference:
            btnattrs['data-reference'] = self.reference

        if self.asnavitem:
            # Navbar Dropdown
            wrappercl.append('nav-item')
            wrapper = ListItem(
                ident=f'{self.ident}-dropdown',
                cl=' '.join(wrappercl),
                style=self.style,
                attrs=self.attrs
            )

            btnattrs['role'] = 'button'
            wrapper.addelement(Anchor(
                cl='nav-link dropdown-toggle',
                href='#',
                ident=self.ident,
                attrs=btnattrs
            ))

        elif self.split:
            # Split Button
            wrapper = ButtonGroup(
                ident=f'{self.ident}-dropdown',
                cl=' '.join(wrappercl),
                style=self.style,
                attrs=self.attrs
            )
            wrapper.addelement(Button(
                self.text,
                ident=self.ident,
                severity=self.severity,
                size=self.size,
            ))
            wrapper.addelement(Button(
                '<span class="sr-only">Toggle Dropdown</span>',
                ident=self.ident,
                severity=self.severity,
                size=self.size,
                cl='dropdown-toggle dropdown-toggle-split',
                attrs=btnattrs
            ))

        else:
            if self.asbtngrp:
                # Single button
                wrapper = ButtonGroup(
                    ident=f'{self.ident}-dropdown',
                    cl=' '.join(wrappercl),
                    style=self.style,
                    attrs=self.attrs
                )
            else:
                # Single button
                wrapper = Div(
                    ident=f'{self.ident}-dropdown',
                    cl=' '.join(wrappercl),
                    style=self.style,
                    attrs=self.attrs
                )
            wrapper.addelement(Button(
                self.text,
                ident=self.ident,
                severity=self.severity,
                size=self.size,
                cl='dropdown-toggle',
                attrs=btnattrs
            ))

        if self.align == 'left':
            menucl = 'dropdown-menu'

        elif self.align == 'right':
            menucl = 'dropdown-menu dropdown-menu-right'

        # Menu
        menu = Div(cl=menucl, attrs={'aria-labelledby': self.ident})
        wrapper.addelement(menu)

        for child in self._children:
            if type(child) == DropdownItem:
                menu.addelement(child)
            else:
                wrapper.addelement(child)

        return str(wrapper)


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
        if self.divider:
            output = ['<div']
        elif self.header:
            output = ['<h6']
        else:
            output = ['<a href="#"']

        if self.ident:
            output.append(f' id="{self.ident}"')

        cls = []

        if self.header:
            cls.append("dropdown-header")
        elif self.divider:
            cls.append("dropdown-divider")
        elif self.disabled:
            cls.append("dropdown-item disabled")
        else:
            cls.append('dropdown-item')

        if self.cl:
            cls.append(self.cl)

        if len(cls) > 0:
            output.append(f' class="{" ".join(cls)}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append('>')

        if self.text:
            output.append(str(self.text))

        output.extend([str(child) for child in self._children])

        if self.divider:
            output.append('</div>')
        elif self.header:
            output.append('</h6>')
        else:
            output.append('</a>')

        return "".join(output)
