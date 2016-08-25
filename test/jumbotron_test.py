from sofi.ui import Jumbotron

def test_basic():
    assert(str(Jumbotron()) == "<div class=\"jumbotron\"></div>")

def test_text():
    assert(str(Jumbotron("text")) == "<div class=\"jumbotron\">text</div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Jumbotron("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"jumbotron abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</div>")
