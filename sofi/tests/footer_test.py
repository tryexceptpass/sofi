from .. import Footer

def test_basic():
    assert(str(Footer()) == "<footer></footer>")

def test_text():
    assert(str(Footer("text")) == "<footer>text</footer>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Footer("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<footer id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</footer>")
