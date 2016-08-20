from sofi.ui import Variable

def test_basic():
    assert(str(Variable()) == "<var></var>")

def test_text():
    assert(str(Variable("text")) == "<var>text</var>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Variable("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<var id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</var>")
