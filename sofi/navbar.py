from .element import Element

class Navbar(Element):
    """Implements the navbar component"""

    def __init__(self, brand="Brand", inverse=False, fixed=None, static=False, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.brand = brand
        self.inverse = inverse
        self.fixed = fixed
        self.static = static

        self.links = []

    def addnavlink(self, a, active=False, align='left', separator=False, cl=None, ident=None, style=None):
        link = ["<li"]
        classes = []

        if ident:
            link.append(' id="')
            link.append(ident)
            link.append('"')

        if separator:
            link.append(' role="separator" ')
            classes.append("separator")

        if active:
            classes.append("active")

        if align == 'right':
            classes.append("navbar-right")

        if cl:
            classes.append(cl)

        if len(classes) > 0:
            link.append(' class="')
            link.append(" ".join(classes))
            link.append('"')

        if style:
            link.append(' style="')
            link.append(style)
            link.append('"')

        link.append('>')

        link.append(str(a))
        link.append('</li>')

        self.links.append("".join(link))

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
        output.append('">')

        output.append('<div class="container-fluid">')

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
        output.append('<ul class="nav navbar-nav">')
                        #<li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
        for link in self.links:
            output.append(link)

        output.append('</ul>')

        output.append('</div>')
        output.append('</div>')
        output.append('</nav>')

        return "".join(output)
