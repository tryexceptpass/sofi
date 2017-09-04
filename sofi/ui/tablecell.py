from .element import Element

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
            output = [ "<th" ]
        else:
            output = [ "<td" ]

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
