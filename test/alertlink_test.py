from sofi.ui import AlertLink

def test_basic():
    assert(str(AlertLink()) == "<a class=\"alert-link\" href=\"#\"></a>")

def test_text():
    assert(str(AlertLink("This is link")) == "<a class=\"alert-link\" href=\"#\">This is link</a>")

def test_custom_class_ident_style_and_attrs():
    assert(str(AlertLink(text="This is link", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<a id=\"123\" class=\"alert-link abclass\" href=\"#\" style=\"font-size:0.9em;\" data-test=\"abc\">This is link</a>")
