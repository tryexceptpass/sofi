from sofi.ui import Deleted

def test_basic():
    assert(str(Deleted()) == "<del></del>")

def test_text():
    assert(str(Deleted("text")) == "<del>text</del>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Deleted("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<del id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</del>")
