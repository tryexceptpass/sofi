from .element import Element
from .anchor import Anchor

class AlertLink(Anchor):
    """Implements the AlertLink <a class="alert-link"> tag"""

    def __init__(self, text=None, href="#", cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.href = href

    def __repr__(self):
        return "<AlertLink(href='" + self.href + "')>"

    def __str__(self):
        classes = [ "alert-link" ]

        if self.cl:
            classes.append(self.cl)

        return str(Anchor(text=self.text, href=self.href, cl=" ".join(classes), ident=self.ident,
                    style=self.style, attrs=self.attrs))
