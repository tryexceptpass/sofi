from .. import Table

def test_basic():
    assert(str(Table()) == "<table class=\"table\"></table>")

def test_striped():
    assert(str(Table(striped=True)) == "<table class=\"table table-striped\"></table>")

def test_bordered():
    assert(str(Table(bordered=True)) == "<table class=\"table table-bordered\"></table>")

def test_condensed():
    assert(str(Table(condensed=True)) == "<table class=\"table table-condensed\"></table>")

def test_hover():
    assert(str(Table(hover=True)) == "<table class=\"table table-hover\"></table>")

def test_responsive():
    assert(str(Table(striped=True, responsive=True)) == "<div class=\"table-responsive\"><table class=\"table table-striped\"></table></div>")

def test_custom_class_ident_and_style():
    assert(str(Table(striped=True, bordered=True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<table id=\"123\" class=\"table table-striped table-bordered abclass\" style=\"font-size:0.9em;\"></table>")