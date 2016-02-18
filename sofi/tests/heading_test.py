from .. import Heading

def test_basic():
    assert(str(Heading()) == "<h1></h1>")

def test_size():
    assert(str(Heading(5)) == "<h5></h5>")

def test_text():
    assert(str(Heading(3, "text")) == "<h3>text</h3>")

def test_custom_class_ident_and_style():
    assert(str(Heading(2, "text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<h2 id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</h2>")
