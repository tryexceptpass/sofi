from sofi.ui import Label

def test_basic():
    assert(str(Label()) == "<span class=\"label label-default\"></span>")

def test_text():
    assert(str(Label("test")) == "<span class=\"label label-default\">test</span>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Label("test", ident='123', cl="testing", style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<span id=\"123\" class=\"label label-default testing\" style=\"font-size:0.9em;\" data-test=\"abc\">test</span>")
