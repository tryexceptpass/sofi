from .element import Element
from .div import Div

class Well(Element):
    """Implements the Bootstrap Well <div class="well">"""

    def __init__(self, text=None, size=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.text = text

    def __repr__(self):
        return "<Well(text='" + self.text + "')>"

    def __str__(self):
        classes = [ "well" ]

        if self.size:
            if self.size == "large" or self.size == "lg":
                classes.append("well-lg")
            elif self.size == "small" or self.size == "sm":
                classes.append("well-sm")

        if self.cl:
            classes.append(self.cl)

        return str(Div(text=self.text, cl=" ".join(classes), ident=self.ident, style=self.style,
                    attrs=self.attrs))
