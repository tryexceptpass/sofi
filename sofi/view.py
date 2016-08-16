from .element import Element
from .navbar import Navbar

class View(Element):
    """Main object representing a webpage"""

    def __init__(self, bscss="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
                       bsjs="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js",
                       jquery="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"):
        self.children = list()

        self.bootstrapcss = bscss
        self.bootstrapjs = bsjs
        self.jquery = jquery

    def __repr__(self):
        return "<View>"

    def __str__(self):
        head = [ "<link href=\"", self.bootstrapcss, "\" rel=\"stylesheet\">" ]
        body = []

        for child in self.children:
            if type(child) == Navbar:
                if child.fixed == "top":
                    head.append('<style>/* Added to make room for the navbar at top */\nbody { padding-top: 70px; }\n</style>')

            body.append(str(child))

        output = []
        output.append('<head>')
        output.extend(head)
        output.append('</head><body>')
        output.extend(body)
        output.append("</body>")

        return "".join(output)
