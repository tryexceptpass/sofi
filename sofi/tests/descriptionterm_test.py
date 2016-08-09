from .. import DescriptionTerm

def test_basic():
    assert(str(DescriptionTerm()) == "<dt></dt>")

def test_text():
    assert(str(DescriptionTerm("text")) == "<dt>text</dt>")

def test_custom_class_ident_style_and_attrs():
    assert(str(DescriptionTerm("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<dt id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</dt>")
