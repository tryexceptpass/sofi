from .element import Element
from .row import Row


class Container(Element):
    """Implements a container tag of form <div class=\"container\"> or
    <div class=\"container-fluid\">"""

    def __init__(self, fluid=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.fluid = fluid

    def newrow(self, element):
        r = Row()
        r.addelement(element)
        self.addelement(r)

        return r

    def __repr__(self):
        return f"<Container(fluid={self.fluid})>"

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="container')

        if self.fluid:
            output.append("-fluid")

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)
