from .element import Element
from .anchor import Anchor
from .heading import Heading
from .paragraph import Paragraph

ITEMSEVS = { 'danger':  'list-group-item-danger',
             'success': 'list-group-item-success',
             'info':    'list-group-item-info',
             'warning': 'list-group-item-warning',
             'default': ''
           }

class ListGroup(Element):
    """Implements the Bootstrap ListGroup as and unordered list or div with class list-group"""

    def __init__(self, linkify=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.linkify = linkify
        self.items = list()

    def additem(self, item, severity=None, disabled=False, heading=None):
        """Add a ListItem to the group which adjusts itself as needed for display based on ListGroup properties"""

        if item.cl:
            item.cl = item.cl + " list-group-item"
        else:
            item.cl = "list-group-item"

        if severity:
            if severity in ITEMSEVS:
                severity = ITEMSEVS[severity]
            else:
                severity = ITEMSEVS['default']

            item.cl = item.cl + " " + severity

        if disabled:
            item.cl = item.cl + " disabled"

        if heading:
            item.addelement(Heading(4, heading, cl='list-group-item-heading'))
            item.addelement(Paragraph(item.text, cl='list-group-item-text'))
            item.text = None

        self.items.append(item)

    def __repr__(self):
        return "<ListGroup(linkify=" + str(self.linkify) + ")>"

    def __str__(self):
        output = [ "<ul" ]

        if self.linkify:
            output = [ "<div" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"list-group")
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

        for item in self.items:
            if self.linkify:
                a = Anchor(text=item.text, cl=item.cl, ident=item.ident, style=item.style, attrs=item.attrs)

                for child in item._children:
                    a.addelement(child)

                output.append(str(a))
            else:
                output.append(str(item))

        for child in self._children:
            output.append(str(child))

        if self.linkify:
            output.append("</div>")
        else:
            output.append("</ul>")

        return "".join(output)
