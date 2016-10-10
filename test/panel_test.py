from sofi.ui import Panel, Table, ListGroup
import pytest

def test_basic():
    assert(str(Panel()) == "<div class=\"panel panel-default\"><div class=\"panel-body\"></div></div>")

def test_sev_primary():
    assert(str(Panel(severity="primary")) == "<div class=\"panel panel-primary\"><div class=\"panel-body\"></div></div>")

def test_sev_warning():
    assert(str(Panel(severity="warning")) == "<div class=\"panel panel-warning\"><div class=\"panel-body\"></div></div>")

def test_sev_danger():
    assert(str(Panel(severity="danger")) == "<div class=\"panel panel-danger\"><div class=\"panel-body\"></div></div>")

def test_sev_success():
    assert(str(Panel(severity="success")) == "<div class=\"panel panel-success\"><div class=\"panel-body\"></div></div>")

def test_sev_info():
    assert(str(Panel(severity="info")) == "<div class=\"panel panel-info\"><div class=\"panel-body\"></div></div>")

def test_title():
    assert(str(Panel(title="TITLE")) == "<div class=\"panel panel-default\"><div class=\"panel-heading\">TITLE</div><div class=\"panel-body\"></div></div>")

def test_heading_footer():
    assert(str(Panel(title="TITLE", footer="FOOTER")) == "<div class=\"panel panel-default\"><div class=\"panel-heading\">TITLE</div><div class=\"panel-body\"></div><div class=\"panel-footer\">FOOTER</div></div>")

def test_table():
    p = Panel(title="TITLE")
    p.settable(Table(hover=True))
    assert(str(p) == "<div class=\"panel panel-default\"><div class=\"panel-heading\">TITLE</div><div class=\"panel-body\"></div><table class=\"table table-hover\"></table></div>")

def test_table_bad_type():
    with pytest.raises(TypeError) as e:
        p = Panel()
        p.settable("abc")

def test_listgroup():
    p = Panel(title="TITLE")
    p.setlistgroup(ListGroup())
    assert(str(p) == "<div class=\"panel panel-default\"><div class=\"panel-heading\">TITLE</div><div class=\"panel-body\"></div><ul class=\"list-group\"></ul></div>")

def test_listgroup_bad_type():
    with pytest.raises(TypeError) as e:
        p = Panel()
        p.settable("abc")

def test_custom_class_ident_style_and_attrs():
    assert(str(Panel("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<div id=\"123\" class=\"panel panel-default abclass\" style=\"font-size:0.9em;\"><div id=\"123-panel-heading\" class=\"panel-heading\">text</div><div id=\"123-panel-body\" class=\"panel-body\"></div></div>")
