class Element(Element):
    """Base HTML tag element"""

    def __init__(self, cl=None, ident=None, style=None):
        """Create a base element where cl is a space separated class attribute,
           ident is the element id and style is a CSS style string"""

        self.cl = cl
        self.ident = ident
        self.style = style

        self.children = list()


    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<Element(cl='" + self.cl + "',ident='" + self.ident + "',children=" + str(len(self.chidren)) + ")>"

    def addelement(self, item):
        """Add a child element to this tag"""

        if item is not None:
            self.children.append(item)
