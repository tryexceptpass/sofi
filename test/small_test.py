from sofi.ui import Small

def test_basic():
    assert(str(Small()) == "<small></small>")

def test_text():
    assert(str(Small("text")) == "<small>text</small>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Small("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<small id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</small>")
