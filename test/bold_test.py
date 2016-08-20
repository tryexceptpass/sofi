from sofi.ui import Bold

def test_basic():
    assert(str(Bold()) == "<strong></strong>")

def test_text():
    assert(str(Bold("text")) == "<strong>text</strong>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Bold("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<strong id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</strong>")
