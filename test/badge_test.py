from sofi.ui import Badge

def test_basic():
    assert(str(Badge()) == "<span class=\"badge\"></span>")

def test_text():
    assert(str(Badge("2")) == "<span class=\"badge\">2</span>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Badge("2", ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<span class=\"badge\" id=\"123\" style=\"font-size:0.9em;\" data-test=\"abc\">2</span>")
