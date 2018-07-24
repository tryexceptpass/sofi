from .element import Element
from .lists import ListGroup
from .anchor import Anchor
from .image import Image


class Card(Element):
    """Implements a Bootstrap card"""

    TEXT_ALIGNMENT = {
        'center': 'text-center',
        'right': 'text-right'
    }

    SEVERITIES = {
        'danger': 'bg-danger',
        'success': 'bg-success',
        'info': 'bg-info',
        'warning': 'bg-warning',
        'primary': 'bg-primary',
        'secondary': 'bg-secondary',
        'light': 'bg-light',
        'dark': 'bg-dark',
    }

    def __init__(self, header=None, title=None, subtitle=None, text=None, footer=None, textalign=None, severity=None,
                 cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if textalign is not None and textalign not in Card.TEXT_ALIGNMENT:
            raise ValueError("Unknown textalign")

        if severity is not None and severity not in Card.SEVERITIES:
            raise ValueError("Unknown severity")

        self.textalign = textalign
        self.severity = severity
        self.text = text

        self.header = header
        self.header_class = None
        self.header_style = None

        self.footer = footer
        self.footer_class = None
        self.footer_style = None

        self.title = title
        self.title_heading = 5
        self.title_class = None
        self.title_style = None

        self.subtitle = subtitle
        self.subtitle_heading = 6
        self.subtitle_class = None
        self.subtitle_style = None

        self._links = {}
        self.image = None
        self.image_bottom = False
        self.image_overlay = False
        self.listgroup = None

    def setheader(self, header, cl=None, style=None):
        self.header = header
        self.header_class = None
        self.header_style = None

    def setfooter(self, footer, cl=None, style=None):
        self.footer = footer
        self.footer_class = None
        self.footer_style = None

    def settitle(self, title, heading=5, cl=None, style=None):
        self.title = title
        self.title_heading = heading
        self.title_class = cl
        self.title_style = style

    def setsubtitle(self, subtitle, heading=6, cl=None, style=None):
        self.subtitle = subtitle
        self.subtitle_heading = heading
        self.subtitle_cl = cl
        self.subtitle_style = style

    def setimage(self, img, bottom=False, overlay=False):
        if isinstance(img, Image):
            img.cl = f'card-img-{"bottom" if bottom else "top"} {img.cl}'
        else:
            img = Image(src=img, cl='card-img-{"bottom" if bottom else "top"}')

        self.image = img
        self.image_bottom = bottom
        self.image_overlay = overlay

    def setlistgroup(self, lg):
        if not isinstance(lg, ListGroup):
            raise TypeError('The "lg" parameter must be a ListGroup')

        self.listgroup = lg

    def addlink(self, link=None):
        if isinstance(link, Anchor):
            link.cl = f'card-link {link.cl}'
        else:
            link = Anchor(href=link, cl='card-link')

        self._links[link.href] = link

    def removelink(self, link):
        if isinstance(link, Anchor):
            del self.link[link.href]
        else:
            del self.link[link]

    def __repr__(self):
        return '<Card()>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="card')

        if self.textalign:
            output.append(f" {Card.TEXT_ALIGNMENT[self.textalign]}")

        if self.severity:
            output.append(f" {Card.SEVERITIES[self.severity]}")

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        if self.header:
            output.append('<div class="card-header')
            if self.header_class:
                output.append(f' {self.header_class}')
            output.append('"')
            if self.ident:
                output.append(f' id="{self.ident}-header"')
            if self.header_style:
                output.append(f' style="{self.header_style}"')
            output.append(f'>{self.header}</div>')

        if self.image and not self.image_bottom:
            output.append(f'{self.image}')

        if self.title or self.subtitle or self.text or len(self._children) > 0:
            output.append(f'<div id={self.ident}-body class="card-{"img-overlay" if self.image_overlay else "body"}">'
                          if self.ident else '<div class="card-body">')

            if self.title:
                output.append(f'<h{self.title_heading} class="card-title{" mb-2" if not self.subtitle else ""}')
                if self.title_class:
                    output.append(f' {self.title_class}')
                output.append('"')
                if self.ident:
                    output.append(f' id="{self.ident}-title"')
                if self.title_style:
                    output.append(f' style="{self.title_style}"')
                output.append(f'>{self.title}</h{self.title_heading}>')

            if self.subtitle:
                output.append(f'<h{self.subtitle_heading} class="card-subtitle mb-2 text-muted')
                if self.subtitle_class:
                    output.append(f' {self.subtitle_class}')
                output.append('"')
                if self.ident:
                    output.append(f' id="{self.ident}-subtitle"')
                if self.subtitle_style:
                    output.append(f' style="{self.subtitle_style}"')
                output.append(f'>{self.subtitle}</h{self.subtitle_heading}>')

            if self.text:
                output.append(f'<p class="card-text">{self.text}</p>')

            output.extend([str(child) for child in self._children])

            output.append("</div>")

        if self.listgroup:
            output.append(f"{self.listgroup}")

        if len(self._links) > 0:
            output.append(f'<div class="card-body">')
            output.extend([str(link) for link in self._links.values()])
            output.append('</div>')

        if self.image and self.image_bottom:
            output.append(f'{self.image}')

        if self.footer:
            output.append('<div class="card-footer')
            if self.footer_class:
                output.append(f' {self.footer_class}')
            output.append('"')
            if self.ident:
                output.append(f' id="{self.ident}-footer"')
            if self.footer_style:
                output.append(f' style="{self.footer_style}"')
            output.append(f'>{self.footer}</div>')

        output.append("</div>")

        return "".join(output)


class CardGroup(Element):
    """Implements the Bootstrap card group"""

    def __init__(self, cards, valign=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self._cards = cards

    def addcard(self, card):
        if not isinstance(card, Card):
            raise TypeError()

        return self._cards.append(card)

    def __repr__(self):
        return '<CardGroup()>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="card-group')

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(card) for card in self._cards])

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)


class CardDeck(Element):
    """Implements the Bootstrap card deck"""

    def __init__(self, cards, valign=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self._cards = cards

    def addcard(self, card):
        if not isinstance(card, Card):
            raise TypeError()

        return self._cards.append(card)

    def __repr__(self):
        return '<CardDeck()>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="card-deck')

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(card) for card in self._cards])

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)


class CardColumns(Element):
    """Implements the Bootstrap card deck"""

    def __init__(self, cards, valign=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self._cards = cards

    def addcard(self, card):
        if not isinstance(card, Card):
            raise TypeError()

        return self._cards.append(card)

    def __repr__(self):
        return '<CardColumns()>'

    def __str__(self):
        output = ["<div "]

        if self.ident:
            output.append(f'id="{self.ident}" ')

        output.append('class="card-columns')

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(card) for card in self._cards])

        output.extend([str(child) for child in self._children])

        output.append("</div>")

        return "".join(output)
