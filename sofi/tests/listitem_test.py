from .. import ListItem

def test_basic():
    assert(str(ListItem()) == "<li></li>")

def test_text():
    assert(str(ListItem("text")) == "<li>text</li>")

def test_custom_class_ident_style_and_attrs():
    assert(str(ListItem("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<li id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</li>")
