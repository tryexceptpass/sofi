from .. import Span

def test_basic():
    assert(str(Span()) == "<span></span>")

def test_text():
    assert(str(Span("text")) == "<span>text</span>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Span("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<span id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</span>")
