from sofi.ui import Div

def test_basic():
    assert(str(Div()) == "<div></div>")

def test_text():
    assert(str(Div("text")) == "<div>text</div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Div("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</div>")
