from .element import Element
from .span import Span

class Badge(Element):
    """Implement Boostrap Badge <span class="badge">"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text

    def __repr__(self):
        return "<Badge(text='" + self.text + "')>"

    def __str__(self):
        badge_cl = "badge"

        if self.cl:
            badge_cl = badge_cl + " " + self.cl

        return str(Span(text=self.text, cl=badge_cl, ident=self.ident,
                        style=self.style, attrs=self.attrs))
