from sofi.ui import TableRow

def test_basic():
    assert(str(TableRow()) == "<tr></tr>")

def test_text():
    assert(str(TableRow("text")) == "<tr>text</tr>")

def test_custom_class_ident_style_and_attrs():
    assert(str(TableRow("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<tr id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</tr>")
