from sofi.ui import Row

def test_basic():
    assert(str(Row()) == "<div class=\"row\"></div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Row(cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"row abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"></div>")
