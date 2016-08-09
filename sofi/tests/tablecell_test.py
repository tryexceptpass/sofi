from .. import TableCell

def test_basic():
    assert(str(TableCell()) == "<td></td>")

def test_text():
    assert(str(TableCell("text")) == "<td>text</td>")

def test_custom_class_ident_style_and_attrs():
    assert(str(TableCell("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<td id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</td>")
