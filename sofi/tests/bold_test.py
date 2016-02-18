from .. import Bold

def test_basic():
    assert(str(Bold()) == "<strong></strong>")

def test_text():
    assert(str(Bold("text")) == "<strong>text</strong>")

def test_custom_class_ident_and_style():
    assert(str(Bold("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<strong id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</strong>")