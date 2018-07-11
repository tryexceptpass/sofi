from .element import Element

from base64 import b64encode

class Image(Element):
    """Implements the <img> tag"""

    VARIETIES = {
        'rounded':  'img-rounded',
        'circle':  'img-circle',
        'thumbnail': 'img-thumbnail',
    }

    def __init__(self, src=None, variety=None, width=None, height=None, alt=None, responsive=False, caption=None, captionalign=None, cl=None, ident=None, style=None, attrs=None):
        if variety not in Image.VARIETIES:
            raise ValueError(f"Unknown variety: {variety}")

        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.src = src
        self.variety = variety
        self.width = width
        self.height = height
        self.alt = alt
        self.responsive = responsive
        self.caption = caption
        self.captionalign = captionalign

    def datauri(self, path, type=None):
        """Use a data URI to embed the image in the given path by base64 encoding it. Supports png, jpg and gif formats."""

        media = None
        ext = path.split('.')[-1]

        if ext == "png":
            media = "image/png"
        elif ext == "jpg" or ext == "jpeg":
            media = "image/jpg"
        elif ext == "gif":
            media = "image/gif"
        else:
            raise ValueError("Unknown image format")

        encoded = None
        with open(path, "rb") as img:
            encoded = b64encode(img.read()).decode('utf-8')

        if encoded:
            self.src = f"data:{media};base64,{encoded}"

    def __repr__(self):
        return f'<Image(src="{self.src}")>'

    def __str__(self):
        output = []

        if self.caption:
            output.append('<figure class="figure">')

        output.append("<img")

        if self.src:
            output.append(f'src="{self.src}" ')

        if self.ident:
            output.append(f' id="{self.ident}"')

        classes = []

        if self.variety:
            classes.append(Image.VARIETIES[self.variety])

        if self.responsive:
            classes.append("img-responsive")

        if self.cl:
            classes.append(self.cl)

        if len(classes) > 0:
            output.append(f' class="{" ".join(classes)}"'

        if self.alt:
            output.append(f' alt="{self.alt}"')

        if self.width:
            output.append(f' width="{self.width}"')

        if self.height:
            output.append(f' height="{self.height}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append('>')

        if self.caption:
            if self.captionalign:
                output.append(f'<figcaption class="figure-caption {self.captionalign}>{self.caption}</figcaption></figure>')
            else:
                output.append(f'<figcaption class="figure-caption>{self.caption}</figcaption></figure>')

        return "".join(output)
