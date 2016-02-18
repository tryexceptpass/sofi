from .. import ListItem

def test_basic():
    assert(str(ListItem()) == "<li></li>")

def test_text():
    assert(str(ListItem("text")) == "<li>text</li>")

def test_custom_class_ident_and_style():
    assert(str(ListItem("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<li id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</li>")