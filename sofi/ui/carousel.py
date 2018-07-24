import secrets

from .element import Element
from .image import Image
from .div import Div


class Carousel(Element):
    """Implements a Bootstrap carousel"""

    def __init__(self, controls=False, indicators=False, crossfade=None,
                 interval=None, keyboard=None, pause=None, ride=None, wrap=None,
                 cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.ident = secrets.token_hex(12) if ident is None else ident
        self._items = {}
        self.controls = controls
        self.indicators = indicators
        self.crossfade = crossfade

        self.attrs['data-ride'] = ride if ride else 'carousel'

        if interval:
            self.attrs['data-interval'] = interval

        if keyboard:
            self.attrs['data-keyboard'] = keyboard

        if pause:
            self.attrs['data-pause'] = pause

        if wrap:
            self.attrs['data-wrap'] = wrap

    def additem(self, image, caption=None, active=False, cl=None, ident=None, style=None, attrs=None):
        if not isinstance(image, Image):
            raise TypeError()

        image.cl = f'd-block w-100 {image.cl}'
        item = Div(cl=f'carousel-item{" active" if active else ""}')
        item.addelement(image)

        if caption:
            cap = Div(cl='carousel-caption d-none d-md-block')
            cap.addelement(caption)
            item.addelement(cap)

        self._items[image.src] = item

    def removeitem(self, image):
        del self._items[image.src]

    def __repr__(self):
        return f'<Carousel()>'

    def __str__(self):
        output = [f'<div id="{self.ident}" class="carousel slide']

        if self.crossfade:
            output.append(f" carousel-fade")

        if self.cl:
            output.append(f" {self.cl}")

        output.append('"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        if self.indicators:
            output.append(f'<ol id="{self.ident}-indicators" class="carousel-indicators">')

            for i, item in enumerate(self._items.values()):
                output.extend([
                    f'<li data-target="#{self.ident}" data-slide-to="{i}"',
                    ' class="active"' if 'active' in item.cl else '',
                    '></li>'
                ])

            output.append('</ol>')

        output.append(f'<div id="{self.ident}-inner" class="carousel-inner">')
        output.extend([str(item) for item in self._items.values()])
        output.append("</div>")

        output.extend([str(child) for child in self._children])

        if self.controls:
            output.append(
                f'<a id="{self.ident}-prev" class="carousel-control-prev" href="#{self.ident}" role="button" data-slide="prev">'
                f'<span class="carousel-control-prev-icon" aria-hidden="true"></span>'
                f'<span class="sr-only">Previous</span>'
                f'</a>'
                f'<a id="{self.ident}-nect"class="carousel-control-next" href="#{self.ident}" role="button" data-slide="next">'
                f'<span class="carousel-control-next-icon" aria-hidden="true"></span>'
                f'<span class="sr-only">Next</span>'
                f'</a>'
            )

        output.append("</div>")

        return "".join(output)
