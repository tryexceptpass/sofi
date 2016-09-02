class Element(object):
    """Base HTML tag element"""

    def __init__(self, cl=None, ident=None, style=None, attrs=None):
        """Create a base element where cl is a space separated class attribute,
           ident is the element id and style is a CSS style string"""

        self.cl = cl
        self.ident = ident
        self.style = style
        self.attrs = attrs

        self.children = list()

    def _attrs_to_string(self, attributes):
        """
        A shortcut for generating all the tag attributes (id, class, etc) 
        given a list of (attr_name_in_self, attr_name_in_html) pairs.

        >>> e = Element(cl='container', ident='foo')

        >>> attributes = [
        ...         ('cl', 'class'),
        ...         ('ident', 'id')]

        >>> e._attrs_to_string(attributes)
        'class="container" id="foo"'

        """
        output = []

        for name, as_html in attributes:
            # Grab the value of the `name` attribute from `self`
            value = getattr(self, name, None)
            if value:
                output.append('{}="{}"'.format(as_html, value))

        return ' '.join(output)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<Element(cl='" + self.cl + "',ident='" + self.ident + "',children=" + str(len(self.chidren)) + ")>"

    def addelement(self, item):
        """Add a child element to this tag"""

        if item is not None:
            self.children.append(item)
