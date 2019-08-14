from .element import Element
from .navbar import Navbar
from .fontawesomeicon import FontAwesomeIcon


class View(Element):
    """Main object representing a webpage"""

    def __init__(self, title=None, cl=None, style=None):
        self._children = []

        if title is None:
            self.title = "Sofi"
        else:
            self.title = title

        self.cl = cl
        self.style = style

        self.bootstrapcss = (
            '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" '
            'integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" '
            'crossorigin="anonymous">'
        )
        self.fontawesomecss = (
            '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.9.0/css/all.css" '
            'integrity="sha384-i1LQnF23gykqWXg6jxC2ZbCbUMxyw5gLZY6UiUS98LYV5unm8GWmfkIS6jqJfb4E" '
            'crossorigin="anonymous">'
        )
        self.bootstrapjs = (
            '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" '
            'integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" '
            'crossorigin="anonymous"></script>'
        )
        self.jquery = (
            '<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" '
            'integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8=" '
            'crossorigin="anonymous"></script>'
        )
        self.popperjs = (
            '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" '
            'integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" '
            'crossorigin="anonymous"></script>'
        )
        self.viewport = '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'

    def __repr__(self):
        return "<View()>"

    def __str__(self):
        head = [f'<title>{self.title}</title>{self.bootstrapcss}{self.viewport}']
        body = []

        for child in self._children:
            # If we included FontAwesomeIcons, add the necessary CSS
            if self.haschild(child, FontAwesomeIcon):
                head.append(self.fontawesomecss)

            # If we're using a Navbar fixed to the top of the page, leave room for it in the body
            if type(child) == Navbar:
                if child.fixed == "top":
                    head.append('<style>body{padding-top:70px}</style>')

            body.append(str(child))

        output = [f'<head>{head}</head><body']

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        output.append(f">{body}{self.jquery}{self.popperjs}{self.bootstrapjs}</body>")

        return "".join(output)


class Row(Element):
    """Implements row layout with format <div class="row">"""

    ALIGNMENT = {
        'start': 'justify-content-start',
        'center': 'justify-content-center',
        'end': 'justify-content-end',
        'around': 'justify-content-around',
        'between': 'justify-content-between'
    }
    VERTICAL_ALIGNMENT = {'start': 'align-items-start', 'center': 'align-items-center', 'end': 'align-items-end'}

    def __init__(self, align=None, valign=None, cl=None, ident=None, style=None, attrs=None):
        if align is not None and valign not in Row.ALIGNMENT:
            raise ValueError(f"Unknown alignment: {align}")

        if valign is not None and valign not in Row.VERTICAL_ALIGNMENT:
            raise ValueError(f"Unknown vertical alignment: {valign}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.align = align
        self.valign = valign

    def newcolumn(self, item, **kwargs):
        """Add a new Column to this Row"""

        c = Column(**kwargs)
        c.addelement(item)

        self.addelement(c)

        return c

    def __repr__(self):
        return f'<Row(valign="{self.valign}")>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="row')

        if self.align:
            output.append(f' {Row.ALIGNMENT[self.align]}')

        if self.valign:
            output.append(f' {Row.VERTICAL_ALIGNMENT[self.valign]}')

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(f">{[str(child) for child in self._children]}</div>")

        return "".join(output)


class Column(Element):
    """The column layout element <div class="col-"> where size, count and offset 
    attributes are used to create the class name, i.e.: col-md-4 or col-offset-md-4"""

    VERTICAL_ALIGNMENT = {'start': 'align-self-start', 'center': 'align-self-center', 'end': 'align-self-end'}

    def __init__(self, size='md', count=4, offset=0, valign=None, order=None, cl=None, ident=None, style=None, attrs=None):
        if valign is not None and valign not in Column.VERTICAL_ALIGNMENT:
            raise ValueError(f"Unknown vertical alignment: {valign}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.size = size
        self.count = count
        self.offset = offset
        self.valign = valign
        self.order = order

    def __repr__(self):
        return f'<Column(size={self.size},count={self.count},offset={self.offset})>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append(f'class="col-{self.size}-{self.count}')

        if self.offset > 0:
            output.append(f' col-{self.size}-offset-{self.offset}')

        if self.cl:
            output.append(f" {self.cl}")

        if self.order:
            output.append(f' order-{self.order}')

        if self.valign:
            output.append(f' {Column.VERTICAL_ALIGNMENT[self.valign]}')

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(f">{[str(child) for child in self._children]}</div>")

        return "".join(output)


class Container(Element):
    """Implements a container tag of form <div class="container"> or <div class="container-fluid">"""

    def __init__(self, fluid=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.fluid = fluid

    def newrow(self, element, with_column=True):
        """Add a new Row to this Container"""

        r = Row()

        if with_column:
            r.newcolumn(element)
        else:
            r.addelement(element)

        self.addelement(r)

        return r

    def __repr__(self):
        return f"<Container(fluid={self.fluid})>"

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="container')

        if self.fluid:
            output.append("-fluid")

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(f">{[str(child) for child in self._children]}</div>")

        return "".join(output)
