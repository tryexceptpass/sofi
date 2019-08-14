from .element import Element
from .div import Div
from .span import Span


class Form(Element):
    """Implements the <form> tag"""

    def __init__(self, inline=False, horizontal=False, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.inline = inline
        self.horizontal = horizontal

    def __repr__(self):
        return "<Form(inline=" + self.inline + ",horizontal=" + self.horizontal + ")>"

    def __str__(self):
        output = ["<form"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        cls = []
        if self.inline:
            cls.append('form-inline')

        if self.horizontal:
            cls.append('form-horizontal')

        if self.cl:
            cls.append(self.cl)

        if len(cls) > 0:
            output.append(" class=\"")
            output.append(" ".join(cls))
            output.append("\"")

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

        output.append("</form>")

        return "".join(output)


class FormGroup(Div):
    """Implements <div> tag with class form-group"""

    def __init__(self, text=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(text=text, cl=cl, ident=ident, style=style, attrs=attrs)

    def __repr__(self):
        return "<FormGroup>"

    def __str__(self):
        output = ["<div"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"form-group")
        if self.cl:
            output.append(" ")
            output.append(self.cl)
        output.append("\"")

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

        output.append("</div>")

        return "".join(output)


class Input(Element):
    """Implements <input> tag"""

    _TYPES = [
        "text",
        "password",
        "datetime",
        "datetime-local",
        "date",
        "month",
        "time",
        "week",
        "number",
        "email",
        "url",
        "search",
        "tel",
        "color"
    ]

    _SIZES = {
        "large": "input-lg",
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
        output = ["<input type=\"", self.inputtype, "\""]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"")

        cl = ["form-control"]

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


class Textarea(Element):
    """Implements <textarea> tag"""

    def __init__(self, text=None, rows=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        if text is not None:
            self.addelement(text)

        self.rows = rows

    def __repr__(self):
        return "<Textarea>"

    def __str__(self):
        output = ["<textarea"]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        output.append(" class=\"form-control")

        if self.cl:
            output.append(" ")
            output.append(self.cl)
        output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        if self.rows:
            output.append(" rows=\"" + str(self.rows) + "\"")

        if self.attrs:
            for k in self.attrs.keys():
                output.append(' ' + k + '="' + self.attrs[k] + '"')

        output.append(">")

        for child in self._children:
            output.append(str(child))

        output.append("</textarea>")

        return "".join(output)
