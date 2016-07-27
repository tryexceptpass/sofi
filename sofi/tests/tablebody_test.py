from .. import TableBody

def test_basic():
    assert(str(TableBody()) == "<tbody></tbody>")

def test_custom_class_ident_and_style():
    assert(str(TableBody(cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<tbody id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\"></tbody>")