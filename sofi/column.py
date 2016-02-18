class Column(object):
    """Implements the column layout <div class=\"col-\"> where size, count and offset
    attributes are used to create the class name, i.e.: col-md-4 or col-offset-md-4"""

    def __init__(self, size='md', count=4, offset=0, cl=None, ident=None, style=None):
        self.children = list()

        self.cl = cl
        self.ident = ident
        self.style = style

        self.size = size
        self.count = count
        self.offset = offset

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

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</div>")

        return "".join(output)


    def additem(self, item):
        if item is not None:
            self.children.append(item)
