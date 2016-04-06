from .. import TableFooter

def test_basic():
    assert(str(TableFooter()) == "<tfoot></tfoot>")

def test_custom_class_ident_and_style():
    assert(str(TableFooter(cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<tfoot id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\"></tfoot>")