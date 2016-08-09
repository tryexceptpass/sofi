from .. import Blockquote

def test_basic():
    assert(str(Blockquote()) == "<blockquote></blockquote>")

def test_text():
    assert(str(Blockquote("text")) == "<blockquote>text</blockquote>")

def test_reverse():
    assert(str(Blockquote("text", True)) == "<blockquote class=\"blockquote-reverse\">text</blockquote>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Blockquote("text", True, cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<blockquote id=\"123\" class=\"blockquote-reverse abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</blockquote>")
