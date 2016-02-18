from .. import BasicBlock

def test_basic():
    assert(str(BasicBlock()) == "<pre></pre>")

def test_text():
    assert(str(BasicBlock("text")) == "<pre>text</pre>")

def test_custom_class_ident_and_style():
    assert(str(BasicBlock("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<pre id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</pre>")