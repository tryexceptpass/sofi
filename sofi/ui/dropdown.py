from .element import Element

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

        if self.navbaritem:
            output.append("<li")
        else:
            output.append("<div")

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('-dropdown"')

        output.append(' class="')
        if self.dropup:
            output.append('dropup')
        else:
            output.append('dropdown')

        if self.cl:
            output.append(' ')
            output.append(self.cl)
        output.append('"')

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append('>')

        if self.navbaritem:
            output.append('<a href="#" ')
        else:
            output.append('<button ')

        if self.ident:
            output.append('id="')
            output.append(self.ident)
            output.append('"')

        if self.navbaritem:
            output.append('class="dropdown-toggle" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
        else:
            output.append('class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">')

        output.append(self.text)
        output.append(' <span class="caret"></span>')

        if self.navbaritem:
            output.append('</a>')
        else:
            output.append('</button>')

        output.append('<ul class="dropdown-menu')

        if self.align == 'right':
            output.append(' dropdown-menu-right')

        output.append('">')

        for child in self.children:
            output.append(str(child))

        output.append("</ul>")

        if self.navbaritem:
            output.append("</li>")
        else:
            output.append("</div>")

        return "".join(output)
