from .element import Element
from .row import Row

class Container(Element):
    """Implements a container tag of form <div class=\"container\"> or
    <div class=\"container-fluid\">"""

    def __init__(self, fluid=False, cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

        self.fluid = fluid

    def newrow(self, element):
        r = Row()
        r.addelement(element)
        self.addelement(r)

    def __repr__(self):
        return "<Container(fluid=" + str(self.fluid) + ")>"

    def __str__(self):
        output = [ "<div " ]

        if self.ident:
            output.append("id=\"")
            output.append(self.ident)
            output.append("\" ")

        output.append("class=\"container")

        if self.fluid:
            output.append("-fluid")

        if self.cl:
            output.append(" ")
            output.append(self.cl)

        output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</div>")

        return "".join(output)
