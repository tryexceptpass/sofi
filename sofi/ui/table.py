from .element import Element


class Table(Element):
    """Implements the <table> tag"""

    def __init__(self, striped=False, bordered=False, hover=False, condensed=False, responsive=False, dark=False,
                 caption=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.striped = striped
        self.bordered = bordered
        self.hover = hover
        self.condensed = condensed
        self.responsive = responsive
        self.dark = dark
        self.caption = caption

    def __repr__(self):
        return f'<Table(striped={self.striped},bordered={self.bordered},hover={self.hover},condensed={self.condensed},responsive={self.responsive},dark={self.dark})>'

    def __str__(self):
        output = ["<table"]

        if self.ident:
            output.append(f' id="{self.ident}" ')

        output.append(' class="table')

        cls = []
        if self.striped:
            cls.append('table-striped')

        if self.bordered:
            cls.append('table-bordered')

        if self.hover:
            cls.append('table-hover')

        if self.condensed:
            cls.append('table-condensed')

        if self.dark:
            cls.append('table-dark')

        if self.cl:
            cls.append(self.cl)

        if len(cls) > 0:
            output.append(' {" ".join(cls)}')

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        if self.caption:
            output.append(f"<caption>{self.caption}</caption>")

        output.extend([str(child) for child in self._children])

        output.append("</table>")

        if self.responsive:
            return "<div class=\"table-responsive\">" + "".join(output) + "</div>"
        else:
            return "".join(output)
