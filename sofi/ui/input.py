from .element import Element
from .span import Span

class Input(Element):
    """Implements <input> tag"""

    _TYPES = [ "text", "password", "datetime", "datetime-local", "date", "month", "time", "week", "number", "email", "url", "search", "tel", "color" ]

    _SIZES = { "large": "input-lg",
               "small": "input-sm"
             }

    def __init__(self, inputtype, placeholder=None, readonly=False, size=None, helptext=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if inputtype not in self._TYPES:
            raise ValueError("Unknown input type: " + inputtype)

        self.inputtype = inputtype
        self.placeholder = placeholder
        self.readonly = readonly
        self.size = size
        self.helptext = helptext

    def __repr__(self):
        return "<Input(type='" + self.inputtype + "')>"

    def __str__(self):
        output = [ "<input type=\"", self.inputtype, "\"" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"")

        cl = [ "form-control" ]

        if self.size and self.size in self._SIZES:
            cl.append(self._SIZES[self.size])

        if self.cl:
            cl.append(self.cl)

        output.append(" ".join(cl))
        output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.placeholder:
            output.append(" placeholder=\"" + self.placeholder + "\"")

        if self.readonly:
            output.append(" readonly")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        helpid = "helpblock"
        if self.ident:
            helpid = self.ident + "-" + helpid

        if self.helptext:
            output.append(" aria-describedby=\"")
            output.append(helpid)
            output.append("\"")

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</input>")

        if self.helptext:
            output.append(str(Span(text=self.helptext, ident=helpid, cl="help-block")))

        return "".join(output)
