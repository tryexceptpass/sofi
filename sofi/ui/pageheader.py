from .element import Element
from .div import Div
from .heading import Heading
from .small import Small

class PageHeader(Element):
    """Implements a Bootstrap Page Header <div class="page-header">"""

    def __init__(self, text=None, subtext=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.subtext = subtext

    def __repr__(self):
        return "<PageHeader(text='" + self.text + "')>"

    def __str__(self):

        classes = [ "page-header" ]
        if self.cl:
            classes.append(self.cl)

        pageheader = Div(text="", cl=" ".join(classes), ident=self.ident, style=self.style, attrs=self.attrs)
        if self.text:
            self.text += " "
        h1 = Heading(size=1, text=self.text)

        if self.subtext:
            small = Small(text=self.subtext)
            h1.addelement(small)

        pageheader.addelement(h1)

        return str(pageheader)
