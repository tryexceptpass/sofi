from .element import Element
from .anchor import Anchor
from .text import Heading, Paragraph


class ListGroup(Element):
    """Implements the Bootstrap ListGroup as and unordered list or div with class list-group"""

    ITEMSEVS = {
        'danger': 'list-group-item-danger',
        'success': 'list-group-item-success',
        'info': 'list-group-item-info',
        'warning': 'list-group-item-warning',
        'default': ''
    }

    def __init__(self, linkify=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.linkify = linkify
        self.items = []

    def additem(self, item, severity=None, disabled=False, heading=None):
        """Add a ListItem to the group which adjusts itself as needed for display based on ListGroup properties"""

        if item.cl:
            item.cl = f"{item.cl} list-group-item"
        else:
            item.cl = "list-group-item"

        if severity:
            if severity in ListGroup.ITEMSEVS:
                severity = ListGroup.ITEMSEVS[severity]
            else:
                severity = ListGroup.ITEMSEVS['default']

            item.cl = f"{item.cl} {severity}"

        if disabled:
            item.cl = f"{item.cl} disabled"

        if heading:
            item.addelement(Heading(4, heading, cl='list-group-item-heading'))
            item.addelement(Paragraph(item.text, cl='list-group-item-text'))
            item.text = None

        self.items.append(item)

    def __repr__(self):
        return f"<ListGroup(linkify={self.linkify})>"

    def __str__(self):
        output = ["<div"] if self.linkify else ["<ul"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        output.append(' class="list-group')

        if self.cl:
            output.append(f' {self.cl}')

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        for item in self.items:
            if self.linkify:
                a = Anchor(text=item.text, cl=item.cl, ident=item.ident, style=item.style, attrs=item.attrs)

                for child in item._children:
                    a.addelement(child)

                output.append(str(a))
            else:
                output.append(str(item))

        output.extend([str(child) for child in self._children])

        output.append("</div>" if self.linkify else "</ul>")

        return "".join(output)


class ListItem(Element):
    """Implements <li> tag"""

    def __init__(self, text=None, inline=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.inline = inline

    def __repr__(self):
        return "<ListItem>"

    def __str__(self):
        output = ["<li"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.inline:
            if self.cl is None:
                self.cl = 'list-inline-item'
            else:
                self.cl = f"{self.cl} list-inline-item"

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        if self.text is not None:
            output.append(self.text)

        output.extend([str(child) for child in self._children])

        output.append("</li>")

        return "".join(output)


class OrderedList(Element):
    """Implements <ol> tag"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<OrderedList>"

    def __str__(self):
        output = ["<ol"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</ol>")

        return "".join(output)


class UnorderedList(Element):
    """Implements <ul> tag"""

    def __init__(self, text=None, unstyled=False, inline=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.unstyled = unstyled
        self.inline = inline

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<UnorderedList(unstyled=" + str(self.unstyled) + ",inline=" + str(self.inline) + ")>"

    def __str__(self):
        output = ["<ul"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        classes = []

        if self.unstyled:
            classes.append('list-unstyled')
        
        if self.inline:
            classes.append('list-inline')

        if self.cl:
            classes.append(self.cl)

        output.append(f' class="{" ".join(classes)}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        for child in self._children:
            if isinstance(child, ListItem):
                child.inline = True

        output.extend([str(child) for child in self._children])

        return "".join(output)
