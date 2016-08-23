from sofi.ui import Label

def test_basic():
    assert(str(Label()) == "<span class=\"label label-default\"></span>")

def test_text():
    assert(str(Label("test")) == "<span class=\"label label-default\">test</span>")

def test_danger_severity():
    assert(str(Label("text", "danger")) == "<span class=\"label label-danger\">text</span>")

def test_info_severity():
    assert(str(Label("text", "info")) == "<span class=\"label label-info\">text</span>")

def test_primary_severity():
    assert(str(Label("text", "primary")) == "<span class=\"label label-primary\">text</span>")

def test_success_severity():
    assert(str(Label("text", "success")) == "<span class=\"label label-success\">text</span>")

def test_warning_severity():
    assert(str(Label("text", "warning")) == "<span class=\"label label-warning\">text</span>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Label("test", ident='123', cl="testing", style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<span id=\"123\" class=\"label label-default testing\" style=\"font-size:0.9em;\" data-test=\"abc\">test</span>")
