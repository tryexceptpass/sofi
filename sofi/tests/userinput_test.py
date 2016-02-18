from .. import UserInput

def test_basic():
    assert(str(UserInput()) == "<kbd></kbd>")

def test_text():
    assert(str(UserInput("text")) == "<kbd>text</kbd>")

def test_custom_class_ident_and_style():
    assert(str(UserInput("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<kbd id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</kbd>")