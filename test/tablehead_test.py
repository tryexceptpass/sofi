from sofi.ui import TableHead

def test_basic():
    assert(str(TableHead()) == "<thead></thead>")

def test_custom_class_ident_style_and_attrs():
    assert(str(TableHead(cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<thead id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"></thead>")
