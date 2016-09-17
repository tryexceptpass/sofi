from .element import Element
from .button import Button

class ButtonGroup(Element):
    """Implements a button group <div class=\"btn-group\">"""

    def __init__(self, size=None, vertical=False, justified=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.vertical = vertical
        self.justified = justified

    def __repr__(self):
        return "<ButtonGroup(size=" + self.size + ")>"

    def __str__(self):
        output = [ "<div " ]

        if self.ident:
            output.append('id="')
            output.append(self.ident)
            output.append('" ')

        output.append('class="')

        classes = [ "btn-group" ]

        if self.cl:
            classes.append(self.cl)
        if self.justified:
            classes.append("btn-group-justified")
        if self.vertical:
            classes.append("btn-group-vertical")
        if self.size:
            if self.size == "large" or self.size == "lg":
                classes.append("btn-group-lg")
            elif self.size == "small" or self.size == "sm":
                classes.append("btn-group-sm")
            elif self.size == "xsmall" or self.size == "xs":
                classes.append("btn-group-xs")

        output.append(" ".join(classes))
        output.append('" role="group"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            if self.justified and type(child) == Button:
                bgrp = ButtonGroup()
                bgrp.addelement(child)
                output.append(str(bgrp))
            else:
                output.append(str(child))

        output.append("</div>")

        return "".join(output)
