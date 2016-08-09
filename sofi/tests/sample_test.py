from .. import Sample

def test_basic():
    assert(str(Sample()) == "<samp></samp>")

def test_text():
    assert(str(Sample("text")) == "<samp>text</samp>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Sample("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<samp id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</samp>")
