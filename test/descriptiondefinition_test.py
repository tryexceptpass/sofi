from sofi.ui import DescriptionDefinition

def test_basic():
    assert(str(DescriptionDefinition()) == "<dd></dd>")

def test_text():
    assert(str(DescriptionDefinition("text")) == "<dd>text</dd>")

def test_custom_class_ident_style_and_attrs():
    assert(str(DescriptionDefinition("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<dd id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</dd>")
