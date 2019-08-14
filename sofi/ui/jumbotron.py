from .element import Element


class Jumbotron(Element):
    """Implements the Bootstrap Jumbotron <div class="jumbotron">"""

    def __init__(self, text=None, fluid=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Jumbotron>"

    def __str__(self):
        output = ['<div']

        if self.ident:
            output.append(f' id="{self.ident}"')

        classes = ['jumbotron']

        if self.cl:
            classes.append(self.cl)

        if self.fluid:
            classes.append('jumbotron-fluid')

        output.append(f' class="{" ".join(classes)}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        if self.fluid:
            output.append('><div class="container">')
        else:
            output.append('>')

        output.extend([str(child) for child in self._children])

        if self.fluid:
            output.append('</div></div>')
        else:
            output.append("</div>")

        return "".join(output)
