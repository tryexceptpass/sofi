from .. import Form

def test_basic():
    assert(str(Form()) == "<form></form>")

def test_inline():
    assert(str(Form(inline=True)) == "<form class=\"form-inline\"></form>")

def test_horizontal():
    assert(str(Form(horizontal=True)) == "<form class=\"form-horizontal\"></form>")

def test_custom_class_ident_and_style():
    assert(str(Form(inline=True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<form id=\"123\" class=\"form-inline abclass\" style=\"font-size:0.9em;\"></form>")