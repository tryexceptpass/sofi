from .element import Element

class FontAwesomeIcon(Element):
    """Implements a Font Awesome Icons"""

    def __init__(self, name=None, size=None, fixed=False, animation=None,
                 rotate=None, flip=None, border=False, pull=None,
                 cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.name = name
        self.size = size
        self.fixed = fixed
        self.animation = animation
        self.rotate = rotate
        self.flip = flip
        self.border = border
        self.pull = pull

    def __repr__(self):
        return "<Icon(name='" + self.name + "')>"

    def __str__(self):

        output = [ "<i" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        classes = ["fa"]

        if self.name:
            classes.append("fa-" + self.name)

        if self.animation:
            classes.append("fa-" + self.animation)

        if self.rotate:
            classes.append("fa-rotate-" + self.rotate)

        if self.border:
            classes.append("fa-border")

        if self.pull:
            classes.append("fa-pull-" + self.pull)

        if self.flip:
            classes.append("fa-flip-" + self.flip)

        if self.size:
            classes.append("fa-" + self.size)

        if self.fixed:
            classes.append("fa-fw")

        if self.cl:
            classes.append(self.cl)

        if len(classes) > 0:
            output.append(' class="')
            output.append(" ".join(classes))
            output.append('"')

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</i>")

        return "".join(output)
