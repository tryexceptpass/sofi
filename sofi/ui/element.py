class Element:
    """Base HTML tag element"""

    def __init__(self, cl=None, ident=None, style=None, attrs={}):
        """Create a base element where cl is a space separated class attribute,
           ident is the element id, style is a CSS style string and attrs is a dictionary
           of additional HTML attributes"""

        self.cl = cl
        self.ident = ident
        self.style = style
        self.attrs = attrs

        self._children = []

    def __repr__(self):
        return f'<Element(cl="{self.cl}",ident="{self.ident}",children="{len(self.chidren)}")>'

    def __str__(self):
        return str(self)

    def addelement(self, element):
        """Add a child element to this tag"""

        if element is not None:
            self._children.append(element)
    
    def visible(self, visibility):
        """Show or hide the element while still occupying space in the DOM"""

        if visibility:
            if 'visible' in self.cl:
                return

            self.cl = f"{self.cl.replace('invisible', '').replace('  ', ' ').trim()} visible"
        
        else:
            if 'invisible' in self.cl:
                return

            self.cl = f"{self.cl.replace('visible', '').replace('  ', ' ').trim()} invisible"
    
    def display(self, display):
        """Allow or prevent the element from occupying space in the DOM"""

        if display:
            if 'd-none' not in self.cl:
                return

            self.cl.replace('d-none', '').replace('  ', ' ').trim()
        
        else:
            if 'd-none' in self.cl:
                return

            self.cl = f"{self.cl} d-none"

    def haschild(self, _type):
        """Recurse the Element hierarchy looking for a child of the given type"""

        if type(self) == _type:
            # Found it
            return True

        else:
            # Check its children
            for child in self._children:
                if not isinstance(child, str):
                    result = self.haschild(child, _type)
                    if result:
                        return True

        return False
