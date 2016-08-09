from .. import Strikethrough

def test_basic():
    assert(str(Strikethrough()) == "<s></s>")

def test_text():
    assert(str(Strikethrough("text")) == "<s>text</s>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Strikethrough("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<s id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</s>")
