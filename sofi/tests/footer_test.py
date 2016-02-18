from .. import Footer

def test_basic():
    assert(str(Footer()) == "<footer></footer>")

def test_text():
    assert(str(Footer("text")) == "<footer>text</footer>")

def test_custom_class_ident_and_style():
    assert(str(Footer("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<footer id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</footer>")
