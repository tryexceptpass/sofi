from .. import TableCaption

def test_basic():
    assert(str(TableCaption()) == "<caption></caption>")

def test_text():
    assert(str(TableCaption("text")) == "<caption>text</caption>")

def test_custom_class_ident_style_and_attrs():
    assert(str(TableCaption("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<caption id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</caption>")
