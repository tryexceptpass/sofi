from .element import Element
from .listgroup import ListGroup
from .table import Table

class Panel(Element):
    """Implements a Bootstrap panel"""

    SEVERITIES = { 'danger':  'panel-danger',
                   'success': 'panel-success',
                   'info':    'panel-info',
                   'warning': 'panel-warning',
                   'primary': 'panel-primary',
                   'default': 'panel-default'
                 }

    def __init__(self, title=None, severity=None, heading=False, footer=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if title:
            self.heading = True
            self._heading = title
        else:
            self.heading = heading
            self._heading = None

        self._footer = footer
        self._embed = None
        self.severity = severity

    def setheading(self, heading):
        """Sets the html contents of the Panel Heading"""

        self._heading = heading

    def setfooter(self, footer):
        """Sets the html contents of the Panel Footer"""

        self._footer = footer

    def settable(self, table):
        """Embeds the Table within the panel outside of the panel body"""

        if isinstance(table, Table):
            self._embed = table
        else:
            raise TypeError("table must be of type Table")

    def setlistgroup(self, listgroup):
        """Embeds the ListGroup within the panel outside of the panel body"""

        if isinstance(listgroup, ListGroup):
            self._embed = listgroup
        else:
            raise TypeError("listgroup must be of type ListGroup")

    def __repr__(self):
        return '<Panel(text="' + self.text + '")>'

    def __str__(self):
        output = []

        output.append("<div")

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        classes = [ "panel" ]
        output.append(' class="')
        if self.severity:
            classes.append(Panel.SEVERITIES[self.severity])
        else:
            classes.append(Panel.SEVERITIES['default'])
        if self.cl:
            classes.append(self.cl)
        output.append(" ".join(classes))
        output.append('"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append('>')

        if self.heading:
            output.append('<div')
            if self.ident:
                output.append(' id="')
                output.append(self.ident + "-" + "panel-heading")
                output.append('"')
            output.append(' class="panel-heading">')
            output.append(str(self._heading))
            output.append('</div>')

        output.append('<div')
        if self.ident:
            output.append(' id="')
            output.append(self.ident + "-" + "panel-body")
            output.append('"')
        output.append(' class="panel-body">')

        for child in self._children:
            output.append(str(child))

        output.append('</div>')

        if self._embed:
            output.append(str(self._embed))

        if self._footer:
            output.append('<div class="panel-footer">')
            output.append(str(self._footer))
            output.append('</div>')


        output.append("</div>")

        return "".join(output)
