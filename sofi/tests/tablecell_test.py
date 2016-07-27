from .. import TableCell

def test_basic():
    assert(str(TableCell()) == "<td></td>")

def test_text():
    assert(str(TableCell("text")) == "<td>text</td>")

def test_custom_class_ident_and_style():
    assert(str(TableCell("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<td id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\">text</td>")