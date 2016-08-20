from sofi.ui import BasicBlock

def test_basic():
    assert(str(BasicBlock()) == "<pre></pre>")

def test_text():
    assert(str(BasicBlock("text")) == "<pre>text</pre>")

def test_custom_class_ident_style_and_attrs():
    assert(str(BasicBlock("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<pre id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</pre>")
