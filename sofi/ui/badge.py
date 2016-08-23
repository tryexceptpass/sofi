from .element import Element
from .span import Span

class Badge(Element):
    """Implement Badges"""

    def __init__(self, text=None, ident=None, style=None, attrs=None):
        super().__init__(ident=ident, style=style, attrs=attrs)

        self.text = text
        self.ident = ident
        self.style = style
        self.attrs = attrs

    def __repr__(self):
        return "<Badge text='" + self.text + "'>"

    def __str__(self):
        return str(Span(text=self.text,cl="badge",ident=self.ident,
                    style=self.style,attrs=self.attrs))
