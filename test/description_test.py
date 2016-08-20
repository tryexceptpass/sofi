from sofi.ui import Description

def test_basic():
    assert(str(Description()) == "<dl></dl>")

def test_text():
    assert(str(Description("text")) == "<dl>text</dl>")

def test_horizontal():
    assert(str(Description("text", True)) == "<dl class=\"dl-horizontal\">text</dl>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Description("text", True, cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<dl id=\"123\" class=\"dl-horizontal abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</dl>")
