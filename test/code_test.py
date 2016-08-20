from sofi.ui import Code

def test_basic():
    assert(str(Code()) == "<code></code>")

def test_text():
    assert(str(Code("text")) == "<code>text</code>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Code("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<code id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</code>")
