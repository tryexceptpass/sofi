from .. import Mark

def test_basic():
    assert(str(Mark()) == "<mark></mark>")

def test_text():
    assert(str(Mark("text")) == "<mark>text</mark>")

def test_custom_class_ident_and_style():
    assert(str(Mark("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<mark id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</mark>")