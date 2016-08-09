from .. import Paragraph

def test_basic():
    assert(str(Paragraph()) == "<p></p>")

def test_text():
    assert(str(Paragraph("text")) == "<p>text</p>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Paragraph("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<p id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</p>")
