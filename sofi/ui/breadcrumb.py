from .element import Element


class Breadcrumb(Element):
    """Implements the breadcrumb component <nav aria-label="breadcrumb">"""

    def __init__(self, crumbs, active=False, cl=None, ident=None, style=None, attrs=None):
        """Create a new Breadcrumb using a list of tuples (name, href, active)"""

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.crumbs = crumbs
        self.active = active

    def __repr__(self):
        return f'<Breadcrumb(active="{self.active}")>'

    def __str__(self):
        output = ['<nav aria-label="breadcrumb"']

        if self.ident:
            output.append(f' id="{self.ident}" ')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append('><ol class="breadcrumb">')

        for crumb, link, active in self.crumbs:
            if active:
                output.append(f'<li class="breadcrumb-item active" aria-current="page"><a href="{link}">{crumb}</a></li>')
            else:
                output.append(f'<li class="breadcrumb-item"><a href="{link}">{crumb}</a></li>')

        output.append("</ol></nav>")

        return "".join(output)
