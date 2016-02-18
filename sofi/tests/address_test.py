from .. import Address

def test_basic():
    assert(str(Address()) == "<address></address>")

def test_text():
    assert(str(Address("text")) == "<address>text</address>")

def test_custom_class_ident_and_style():
    assert(str(Address("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<address id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</address>")