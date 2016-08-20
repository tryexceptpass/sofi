from sofi.ui import Anchor

def test_basic():
    assert(str(Anchor()) == "<a href=\"#\"></a>")

def test_text_href():
    assert(str(Anchor("text", "http://localhost/abc")) == "<a href=\"http://localhost/abc\">text</a>")

def test_custom_class_ident_and_style():
    assert(str(Anchor("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<a id=\"123\" class=\"abclass\" href=\"#\" style=\"font-size:0.9em;\">text</a>")
