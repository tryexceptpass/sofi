from .element import Element
from .span import Span

class Label(Element):
    """Implements the <label> tag"""

    SEVERITIES = { 'danger':  'label-danger',
                   'success': 'label-success',
                   'info':    'label-info',
                   'warning': 'label-warning',
                   'primary': 'label-primary',
                   'default': 'label-default'
                 }

    def __init__(self, text=None, severity=None, cl=None, ident=None, style=None, attrs=None):
        super().__init__(cl=cl, ident=ident, style=style, attrs=attrs)

        self.text = text
        self.severity = severity
        self.ident = ident
        self.style = style
        self.attrs = attrs
        self.cl = cl

    def __repr__(self):
        return "<Label(text='" + self.text + "')>"

    def __str__(self):
        
        classes = [ "label" ]
      
        if self.severity:
            classes.append(Label.SEVERITIES[self.severity])
        else:
            classes.append(Label.SEVERITIES['default'])
        if self.cl:
            classes.append(self.cl)
        label_cl = " ".join(classes)
        
        return str(Span(text=self.text, cl=label_cl, ident=self.ident,
                    style=self.style, attrs=self.attrs))

