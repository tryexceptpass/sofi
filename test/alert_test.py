from sofi.ui import Alert

def test_basic():
    assert(str(Alert()) == "<div class=\"alert\" role=\"alert\"></div>")

def test_text():
    assert(str(Alert("This is alert")) == "<div class=\"alert\" role=\"alert\">This is alert</div>")

def test_success_severity():
    assert(str(Alert("This is alert", severity='success')) == "<div class=\"alert alert-success\" role=\"alert\">This is alert</div>")

def test_danger_severity():
    assert(str(Alert("This is alert", severity='danger')) == "<div class=\"alert alert-danger\" role=\"alert\">This is alert</div>")

def test_info_severity():
    assert(str(Alert("This is alert", severity='info')) == "<div class=\"alert alert-info\" role=\"alert\">This is alert</div>")

def test_warning_severity():
    assert(str(Alert("This is alert", severity='warning')) == "<div class=\"alert alert-warning\" role=\"alert\">This is alert</div>")

def test_close_button():
    assert(str(Alert("This is alert", closebtn=True)) == "<div class=\"alert alert-dismissible fade in\" role=\"alert\"><button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>This is alert</div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Alert(text="This is alert", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"alert abclass\" style=\"font-size:0.9em;\" data-test=\"abc\" role=\"alert\">This is alert</div>")
