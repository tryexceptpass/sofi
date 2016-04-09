from .element import Element

class Dropdown(Element):
    """Implements a Bootstrap dropdown tag"""

    def __init__(self, text, dropup=False, align='left', cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

        self.text = text
        self.dropup = dropup
        self.align = align

    def __repr__(self):
        return '<Dropdown(text="' + self.text + ',dropup=' + str(self.dropup) + ')>'

    def __str__(self):
        output = [ "<div" ]

        if self.ident:
            output.append(' id="')
            output.append(self.ident)
            output.append('-dropdown"')

        output.append(' class="')
        if self.dropup:
            output.append('dropup')
        else:
            output.append('dropdown')
        
        if self.cl:
            output.append(' ')
            output.append(self.cl)
        output.append('"')

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append('>')
        
        
        output.append('<button ')
        
        if self.ident:
            output.append('id="')
            output.append(self.ident)
            output.append('"')
        
        output.append('class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">')
        output.append(self.text)
        output.append(' <span class="caret"></span>')
        output.append('</button>')
        
        
        output.append('<ul class="dropdown-menu')
        
        if self.align == 'right':
            output.append(' dropdown-menu-right')
        
        output.append('">')
        
        for child in self.children:
            output.append(str(child))
            
        output.append("</ul>")
        
        
        output.append("</div>")

        return "".join(output)
