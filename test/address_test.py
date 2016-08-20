from sofi.ui import Address

def test_basic():
    assert(str(Address()) == "<address></address>")

def test_text():
    assert(str(Address("text")) == "<address>text</address>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Address("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<address id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</address>")
