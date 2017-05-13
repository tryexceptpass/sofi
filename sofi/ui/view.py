from .element import Element
from .navbar import Navbar
from .fontawesomeicon import FontAwesomeIcon

class View(Element):
    """Main object representing a webpage"""

    def __init__(self, title=None, cl=None, style=None,
                       bscss="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
                       bsjs="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js",
                       jquery="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"):
        self._children = list()

        if title is None:
            self.title = "Sofi"
        else:
            self.title = title

        self.cl = cl
        self.style = style

        self.bootstrapcss = bscss
        self.bootstrapjs = bsjs
        self.jquery = jquery

    def __repr__(self):
        return "<View>"

    def __str__(self):
        head = [ "<title>", self.title, "</title>", "<link href=\"", self.bootstrapcss, "\" rel=\"stylesheet\">" ]
        body = []

        for child in self._children:
            if self.check_for_element_available(child, FontAwesomeIcon):
                head.append('<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet"></link>')

            if type(child) == Navbar:
                if child.fixed == "top":
                    head.append('<style>/* Added to make room for the navbar at top */\nbody { padding-top: 70px; }\n</style>')

            body.append(str(child))

        output = []
        output.append('<head>')
        output.extend(head)
        output.append('</head><body')
        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")
        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")
        output.append(">")
        output.extend(body)
        output.append("</body>")

        return "".join(output)

    def check_for_element_available(self, child, element):
        if type(child) == element:
            return True
        else:
             for obj in child._children:
                 if not isinstance(obj, str):
                     result = self.check_for_element_available(obj, element)
                     if result:
                         return True
        return False
