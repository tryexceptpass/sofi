from .element import Element
from .anchor import Anchor
from .unorderedlist import UnorderedList
from .navbaritem import NavbarItem

class Navbar(Element):
    """Implements the navbar component"""

    def __init__(self, brand="Brand", inverse=False, fixed=None, static=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.brand = brand
        self.inverse = inverse
        self.fixed = fixed
        self.static = static

    def addlink(self, text, href="#", active=False):
        if len(self.children) == 0:
            self.children.append(UnorderedList(cl="nav navbar-nav"))

        if type(self.children[-1]) != UnorderedList:
            self.children.append(UnorderedList(cl="nav navbar-nav"))

        if active:
            self.children[-1].addelement(NavbarItem(text, href, cl='active'))
        else:
            self.children[-1].addelement(NavbarItem(text, href))

        return self.children[-1]

    def addtext(self, text):
        self.children.append(NavbarItem(text))

        return self.children[-1]

    def adddropdown(self, dropdown):
        if len(self.children) == 0:
            self.children.append(UnorderedList(cl="nav navbar-nav"))

        if type(self.children[-1]) != UnorderedList:
            self.children.append(UnorderedList(cl="nav navbar-nav"))

        dropdown.navbaritem = True
        self.children[-1].addelement(dropdown)

    def __repr__(self):
        return "<Navbar(inverse=" + str(self.inverse) + ",fixed=" + str(self.fixed) + ",static=" + str(self.static) + ")>"

    def __str__(self):
        output = ['<nav class="' ]
        classes = ['navbar']

        if self.inverse:
            classes.append("navbar-inverse")
        else:
            classes.append("navbar-default")

        if self.static:
            classes.append('navbar-static-top')
        elif self.fixed == 'top':
            classes.append('navbar-fixed-top')
        elif self.fixed == 'bottom':
            classes.append('navbar-fixed-bottom')

        if self.cl:
            classes.append(self.cl)
        output.append(" ".join(classes))
        output.append('"')

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append('>')

        output.append('<div class="container">')

        output.append('<div class="navbar-header">')
        output.append('<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sofi-navbar-collapse" aria-expanded="false">')
        output.append('<span class="sr-only">Toggle navigation</span>')
        output.append('<span class="icon-bar"></span>')
        output.append('<span class="icon-bar"></span>')
        output.append('<span class="icon-bar"></span>')
        output.append('</button>')
        output.append('<a class="navbar-brand" href="#">')
        output.append(self.brand)
        output.append('</a>')
        output.append('</div>')

        output.append('<div class="collapse navbar-collapse" id="sofi-navbar-collapse" aria-expanded="false">')

        for child in self.children:
            output.append(str(child))

        output.append('</div>')
        output.append('</div>')
        output.append('</nav>')

        return "".join(output)
