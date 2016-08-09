from .. import Inserted

def test_basic():
    assert(str(Inserted()) == "<ins></ins>")

def test_text():
    assert(str(Inserted("text")) == "<ins>text</ins>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Inserted("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<ins id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</ins>")
