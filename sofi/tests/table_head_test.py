from .. import TableHead

def test_basic():
    assert(str(TableHead()) == "<thead></thead>")

def test_custom_class_ident_and_style():
    assert(str(TableHead(cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<thead id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\"></thead>")