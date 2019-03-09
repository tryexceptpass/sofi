from .element import Element
from .div import Div


class ProgressBar(Element):
    def __init__(self, cl=None, ident=None, style=None, attrs=None, valuenow=0, valuemin=0, valuemax=100):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.valuenow = valuenow
        self.valuemin = valuemin
        self.valuemax = valuemax

    def __repr__(self):
        return "<ProgressBar>"

    def __str__(self):
        attrs = {
            "role": "progressbar",
            "aria-valuenow": str(self.valuenow),
            "aria-valuemin": str(self.valuemin),
            "aria-valuemax": str(self.valuemax),
        }

        d = Div(cl="progress")

        cd = Div(ident=self.ident, cl="progress-bar p-50", style=f"width: {self.valuenow}%", attrs=attrs)

        d.addelement(cd)

        return str(d)
