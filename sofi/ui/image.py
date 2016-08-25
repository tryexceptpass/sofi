from .element import Element

class Image(Element):
    """Implements the <img> tag"""

    VARIETIES = {
                  'rounded':  'img-rounded',
                  'circle':  'img-circle',
                  'thumbnail': 'img-thumbnail',
                }

    def __init__(self, src=None, variety=None, width=None, height=None, alt=None, responsive=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.src = src
        self.variety = variety
        self.width = width
        self.height = height
        self.alt = alt
        self.responsive = responsive

    def __repr__(self):
        return "<Image(src='" + self.src + "')>"

    def __str__(self):
        output = [ "<img" ]

        if self.src:
            output.append(' src="')
            output.append(self.src)
            output.append('"')

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('"')

        classes = []

        if self.variety:
            classes.append(Image.VARIETIES[self.variety])

        if self.responsive:
            classes.append("img-responsive")

        if self.cl:
            classes.append(self.cl)

        if len(classes) > 0:
            output.append(' class="')
            output.append(" ".join(classes))
            output.append('"')

        if self.alt:
            output.append(' alt="')
            output.append(self.alt)
            output.append('"')

        if self.width:
            output.append(' width="')
            output.append(self.width)
            output.append('"')

        if self.height:
            output.append(' height="')
            output.append(self.height)
            output.append('"')

        if self.style:
            output.append(' style="')
            output.append(self.style)
            output.append('"')

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append('>')

        return "".join(output)
