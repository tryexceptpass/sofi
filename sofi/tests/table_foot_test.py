from .. import TableFoot

def test_basic():
    assert(str(TableFoot()) == "<tfoot></tfoot>")

def test_custom_class_ident_and_style():
    assert(str(TableFoot(cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<tfoot id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\"></tfoot>")