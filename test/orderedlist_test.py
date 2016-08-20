from sofi.ui import OrderedList

def test_basic():
    assert(str(OrderedList()) == "<ol></ol>")

def test_text():
    assert(str(OrderedList("text")) == "<ol>text</ol>")

def test_custom_class_ident_style_and_attrs():
    assert(str(OrderedList("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<ol id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</ol>")
