from sofi.ui import ButtonToolbar

def test_basic():
    assert(str(ButtonToolbar()) == "<div class=\"btn-toolbar\" role=\"toolbar\"></div>")

def test_custom_class_ident_and_style():
    assert(str(ButtonToolbar(cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<div id=\"123\" class=\"btn-toolbar abclass\" role=\"toolbar\" style=\"font-size:0.9em;\"></div>")
