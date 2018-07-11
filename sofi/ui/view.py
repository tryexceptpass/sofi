from .element import Element
from .navbar import Navbar
from .fontawesomeicon import FontAwesomeIcon


class View(Element):
    """Main object representing a webpage"""

    def __init__(self, title=None, cl=None, style=None):
        self._children = list()

        if title is None:
            self.title = "Sofi"
        else:
            self.title = title

        self.cl = cl
        self.style = style

        self.bootstrapcss = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">'
        self.fontawesomecss = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous">'
        self.bootstrapjs = '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>'
        self.jquery = '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>'
        self.popperjs = '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>'
        self.viewport = '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'

    def __repr__(self):
        return "<View>"

    def __str__(self):
        head = [f'<title>{self.title}</title>{self.bootstrapcss}{self.viewport}']
        body = []

        for child in self._children:
            if self.check_for_element_available(child, FontAwesomeIcon):
                head.append(self.fontawesomecss)

            if type(child) == Navbar:
                if child.fixed == "top":
                    head.append('<style>/* Added to make room for the navbar at top */\nbody {padding-top: 70px; }\n</style>')

            body.append(str(child))

        output = []
        output.append('<head>')
        output.extend(head)
        output.append('</head><body')
        if self.cl:
            output.append(f' class="{self.cl}"')
        if self.style:
            output.append(f' style="{self.style}"')
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
