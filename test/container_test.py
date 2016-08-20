from sofi.ui import Container

def test_basic():
    assert(str(Container()) == "<div class=\"container\"></div>")

def test_fluid():
    assert(str(Container(True)) == "<div class=\"container-fluid\"></div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Container(True, cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"container-fluid abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"></div>")
