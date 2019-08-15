from .element import Element

class Description(Element):
    """Implements <dl> tag"""


    def __init__(self, text=None, horizontal=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.horizontal = horizontal

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<Description(horizontal=" + self.horizontal + ")>"

    def __str__(self):
        output = ["<dl"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.horizontal:
            if self.cl is None:
                self.cl = 'dl-horizontal'
            else:
                self.cl = f'{self.cl} dl-horizontal'

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</dl>")

        return "".join(output)


class DescriptionDefinition(Element):
    """Implements <dd> tag"""


    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<DescriptionDefinition>"

    def __str__(self):
        output = ["<dd"]

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

        output.append("</dd>")

        return "".join(output)


class DescriptionTerm(Element):
    """Implements <dt> tag"""


    def __init__(self, text=None, truncate=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.truncate = truncate

        if text is not None:
            self.addelement(text)

    def __repr__(self):
        return "<DescriptionTerm>"

    def __str__(self):
        output = ["<dt"]

        if self.ident:
            output.append(f' id="{self.ident}"')

        if self.truncate:
            if self.cl is None:
                self.cl = 'text-truncate'
            else:
                self.cl = f'{self.cl} truncate'

        if self.cl:
            output.append(f' class="{self.cl}"')

        if self.style:
            output.append(f' style="{self.style}"')

        if self.attrs:
            output.extend([f' {k}="{v}"' for k, v in self.attrs.items()])

        output.append(">")

        output.extend([str(child) for child in self._children])

        output.append("</dt>")

        return "".join(output)
