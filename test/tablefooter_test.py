from sofi.ui import TableFooter

def test_basic():
    assert(str(TableFooter()) == "<tfoot></tfoot>")

def test_custom_class_ident_style_and_attrs():
    assert(str(TableFooter(cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<tfoot id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"></tfoot>")
