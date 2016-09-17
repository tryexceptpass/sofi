from .element import Element

class Column(Element):
    """Implements the column layout <div class=\"col-\"> where size, count and offset
    attributes are used to create the class name, i.e.: col-md-4 or col-offset-md-4"""

    def __init__(self, size='md', count=4, offset=0, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.count = count
        self.offset = offset

    def __repr__(self):
        return "<Column(size='" + self.size + "',count='" + str(self.count) + "',offset=" + str(self.offset) + ")>"

    def __str__(self):
        output = [ "<div " ]

        if self.ident:
            output.append("id=\"")
            output.append(self.ident)
            output.append("\" ")

        output.append("class=\"col-")
        output.append(str(self.size))
        output.append("-")
        output.append(str(self.count))

        if self.offset > 0:
            output.append(" col-")
            output.append(self.size)
            output.append("-offset-")
            output.append(str(self.offset))

        if self.cl:
            output.append(" ")
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

        output.append("</div>")

        return "".join(output)
