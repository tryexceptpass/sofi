from .. import Cite

def test_basic():
    assert(str(Cite()) == "<cite></cite>")

def test_text():
    assert(str(Cite("text")) == "<cite>text</cite>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Cite("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<cite id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</cite>")
