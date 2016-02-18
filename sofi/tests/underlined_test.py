from .. import Underlined

def test_basic():
    assert(str(Underlined()) == "<u></u>")

def test_text():
    assert(str(Underlined("text")) == "<u>text</u>")

def test_custom_class_ident_and_style():
    assert(str(Underlined("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<u id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</u>")