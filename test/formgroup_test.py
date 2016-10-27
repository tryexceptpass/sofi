from sofi.ui import FormGroup

def test_basic():
    assert(str(FormGroup()) == "<div class=\"form-group\"></div>")

def test_text():
    assert(str(FormGroup("text")) == "<div class=\"form-group\">text</div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(FormGroup("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"form-group abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</div>")
