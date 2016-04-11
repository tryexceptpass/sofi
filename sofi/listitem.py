from .element import Element

class ListItem(Element):
    """Implements <li> tag"""


    def __init__(self, text=None, cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

        self.text = text

    def __repr__(self):
        return "<ListItem>"

    def __str__(self):
        output = [ "<li" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append(">")

        output.append(self.text)
        
        for child in self.children:
            output.append(str(child))

        output.append("</li>")

        return "".join(output)
