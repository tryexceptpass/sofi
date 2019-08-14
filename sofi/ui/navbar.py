from .element import Element
from .span import Span


class Navbar(Element):
    """Implements the navbar component"""

    def __init__(self, brand="Brand", dark=False, fixed=None, sticky=False, right=False,
                 cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.brand = brand
        self.dark = dark
        self.fixed = fixed
        self.sticky = sticky
        self.right = right

    def addlink(self, text, href=None, active=False, disabled=False, ident=None):
        item = NavbarItem(text, href, active=active, disabled=disabled, ident=ident)
        self.addelement(item)

        return item

    def addtext(self, text):
        self.addelement(Span(text, cl='navbar-text'))

    # def adddropdown(self, dropdown):
    #     if len(self._children) == 0:
    #         self.addelement(UnorderedList(cl="nav navbar-nav"))
    #
    #     if type(self._children[-1]) != UnorderedList:
    #         self.addelement(UnorderedList(cl="nav navbar-nav"))
    #
    #     dropdown.navbaritem = True
    #     self._children[-1].addelement(dropdown)

    def __repr__(self):
        return f'<Navbar(dark="{self.dark}", fixed="{self.fixed} + ", sticky="{self.sticky}")>'

    def __str__(self):
        output = ['<nav class="']
        classes = ['navbar', 'navbar-expand-md']

        if self.dark:
            classes.append("navbar-dark bg-dark")
        else:
            classes.append("navbar-light bg-light")

        if self.sticky:
            classes.append('sticky-top')
        elif self.fixed == 'top':
            classes.append('fixed-top')
        elif self.fixed == 'bottom':
            classes.append('fixed-bottom')

        if self.cl:
            classes.append(self.cl)

        output.append(f'{" ".join(classes)}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append('>')

        output.append(f'<a class="navbar-brand mr-5" href="#">{self.brand}</a>')
        output.append(
            '<button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#sofi-navbar-collapse" '
            'aria-controls="sofi-navbar-collapse" aria-expanded="false" aria-label="Toggle Navigation">'
            '<span class="navbar-toggler-icon"></span></button>'
        )
        output.append('<div class="collapse navbar-collapse" id="sofi-navbar-collapse">')
        output.append(f'<div class="navbar-nav{" ml-auto" if self.right else ""}">')

        output.extend([str(child) for child in self._children])

        output.append('</div></div></nav>')

        return "".join(output)


class NavbarItem(Element):
    """Implements an item for a Navbar"""

    def __init__(self, text='', href=None, active=False, disabled=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.href = href
        self.active = active
        self.disabled = disabled

    def __repr__(self):
        if self.href is None:
            return f'<NavbarItem(text="{self.text}")>'
        else:
            return f'<NavbarItem(text="{self.text}", href="{self.href}")>'

    def __str__(self):
        output = ['<a']

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.href:
            output.append(f' href="{self.href}"')

        cls = ['nav-item', 'nav-link']

        if self.cl:
            cls.append(self.cl)

        if self.disabled:
            cls.append('disabled')

        if self.active:
            cls.append('active')

        if len(cls) > 0:
            output.append(f' class="{" ".join(cls)}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append('>')

        output.append(self.text)

        output.extend([str(child) for child in self._children])

        output.append("</a>")

        return "".join(output)
