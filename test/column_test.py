from sofi.ui import Column

def test_basic():
    assert(str(Column()) == "<div class=\"col-md-4\"></div>")

def test_size_count():
    assert(str(Column('lg', 2)) == "<div class=\"col-lg-2\"></div>")

def test_offset():
    assert(str(Column('lg', 2, 3)) == "<div class=\"col-lg-2 col-lg-offset-3\"></div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Column(cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"col-md-4 abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"></div>")
