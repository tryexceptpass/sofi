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


class TableBody(Element):
    """Implements the <tbody> tag"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def addrow(self, *args, **kwargs):
        tr = TableRow(**kwargs)

        for item in args:
            if isinstance(item, Element):
                tr.addelement(item)
            else:
                tr.addelement(TableCell(item))

        self.addelement(tr)

        return tr

    def __repr__(self):
        return "<TableBody>"

    def __str__(self):
        output = ["<tbody"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</tbody>")

        return "".join(output)


class TableCell(Element):
    """Implements <td> and <th> tag"""

    def __init__(self, text=None, head=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

        self.head = head

    def __repr__(self):
        return "<TableCell(head=" + self.head + ")>"

    def __str__(self):
        if self.head:
            output = ["<th"]
        else:
            output = ["<td"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</td>")

        return "".join(output)


class TableFooter(Element):
    """Implements the <tfoot> tag"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<TableFooter>"

    def __str__(self):
        output = ["<tfoot"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</tfoot>")

        return "".join(output)


class TableHead(Element):
    """Implements the <thead> tag"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

    def addrow(self, *args, **kwargs):
        tr = TableRow(**kwargs)

        for item in args:
            if isinstance(item, Element):
                tr.addelement(item)
            else:
                tr.addelement(TableCell(item, head=True))

        self.addelement(tr)

        return tr

    def __repr__(self):
        return "<TableHead>"

    def __str__(self):
        output = ["<thead"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</thead>")

        return "".join(output)


class TableRow(Element):
    """Implements <tr> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text:
            self._children.append(text)

    def __repr__(self):
        return "<TableRow>"

    def __str__(self):
        output = ["<tr"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</tr>")

        return "".join(output)
