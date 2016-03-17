class View(object):
    """Main object representing a webpage"""

    def __init__(self, bscss="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css",
                       bsjs="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js",
                       jquery="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"):
        self.children = list()

        self.bootstrapcss = bscss
        self.bootstrapjs = bsjs
        self.jquery = jquery


    def __str__(self):
        output = [ "<head><link href=\"", self.bootstrapcss, "\" rel=\"stylesheet\"></head><body>" ]

        for child in self.children:
            output.append(str(child))

        #output.append('<script src="')
        #output.append(self.jquery)
        #output.append('"></script>')

        #output.append("<script src=\"")
        #output.append(self.bootstrapjs)
        #output.append("\"></script>")

        #output.append("<script src=\"sofi.js\"></script></body>")

        return "".join(output)

    def additem(self, item):
        if item is not None:
            self.children.append(item)