from .element import Element
from .span import Span


class Badge(Element):
    """Implement Boostrap Badge <span class="badge">"""

    CONTEXTS = {
        'primary': 'badge-primary',
        'secondary': 'badge-secondary',
        'success': 'badge-success',
        'danger': 'badge-danger',
        'warning': 'badge-warning',
        'info': 'badge-info',
        'light': 'badge-light',
        'dark': 'badge-dark',
    }

    def __init__(self, text=None, context=None, pill=False, cl=None, ident=None, style=None, attrs=None):
        if context is not None and context not in Badge.CONTEXTS:
            raise ValueError(f"Unknown badge context: {context}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.pill = pill
        self.context = context

    def __repr__(self):
        return f'<Badge(text="{self.text}")>'

    def __str__(self):
        classes = ["badge"]

        if self.pill:
            classes.append('badge-pill')

        if self.context:
            classes.append(Badge.CONTEXTS[self.context])

        if self.cl:
            classes.append(self.cl)

        return str(Span(text=self.text, cl=" ".join(classes), ident=self.ident, style=self.style, attrs=self.attrs))
