from .element import Element
from .badge import Badge


class Anchor(Element):
    """Implements the <a> tag."""

    def __init__(self, text=None, href="#", badgecontext=None, cl=None, ident=None, style=None, attrs=None):
        if badgecontext is not None and badgecontext not in Badge.CONTEXTS:
            raise ValueError(f"Unknown badge context: {badgecontext}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.href = href
        self.badgecontext = badgecontext

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<Anchor(href='" + self.href + "')>"

    def __str__(self):
        output = ["<a"]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        classes = []

        if self.badgecontext:
            classes.append(f'badge {Badge.CONTEXTS[self.badgecontext]}')

        if self.cl:
            classes.append(self.cl)

        if len(classes) > 0:
            output.append(f' class="{" ".join(classes)}"')

        output.append(f' href="{self.href}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</a>")

        return "".join(output)
