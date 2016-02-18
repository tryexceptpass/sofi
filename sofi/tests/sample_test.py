from .. import Sample

def test_basic():
    assert(str(Sample()) == "<samp></samp>")

def test_text():
    assert(str(Sample("text")) == "<samp>text</samp>")

def test_custom_class_ident_and_style():
    assert(str(Sample("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<samp id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</samp>")