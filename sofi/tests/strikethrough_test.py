from .. import Strikethrough

def test_basic():
    assert(str(Strikethrough()) == "<s></s>")

def test_text():
    assert(str(Strikethrough("text")) == "<s>text</s>")

def test_custom_class_ident_and_style():
    assert(str(Strikethrough("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<s id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</s>")