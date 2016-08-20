from sofi.ui import Italics

def test_basic():
    assert(str(Italics()) == "<em></em>")

def test_text():
    assert(str(Italics("text")) == "<em>text</em>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Italics("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<em id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</em>")
