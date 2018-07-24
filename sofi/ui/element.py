class Element(object):
    """Base HTML tag element"""

    def __init__(self, cl=None, ident=None, style=None, attrs={}):
        """Create a base element where cl is a space separated class attribute,
           ident is the element id and style is a CSS style string"""

        self.cl = cl
        self.ident = ident
        self.style = style
        self.attrs = attrs

        self._children = list()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'<Element(cl="{self.cl}",ident="{self.ident}",children="{len(self.chidren)}")>'

    def addelement(self, item):
        """Add a child element to this tag"""

        if item is not None:
            self._children.append(item)
