from .element import Element
from .div import Div

class Well(Div):
    """Implements the Bootstrap Well <div class="well">"""

    def __init__(self, text=None, size=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(text=text, cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size

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

        self.cl = ' '.join(classes)

        return super().__str__()
