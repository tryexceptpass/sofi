from .. import ButtonDropdown

def test_basic():
    assert(str(ButtonDropdown("text")) == "<div class=\"btn-group\" role=\"group\"><button class=\"btn btn-default dropdown-toggle\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_split():
    assert(str(ButtonDropdown("text", split=True)) == "<div class=\"btn-group\" role=\"group\"><button class=\"btn btn-default\">text</button><button class=\"btn btn-default dropdown-toggle\" data-toggle=\"dropdown\"><span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_danger_severity_large():
    assert(str(ButtonDropdown("text", severity="danger", size="large")) == "<div class=\"btn-group\" role=\"group\"><button class=\"btn btn-danger btn-lg dropdown-toggle\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_info_severity_small():
    assert(str(ButtonDropdown("text", severity="info", size="small")) == "<div class=\"btn-group\" role=\"group\"><button class=\"btn btn-info btn-sm dropdown-toggle\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_primary_severity_xsmall():
    assert(str(ButtonDropdown("text", severity="primary", size="xsmall")) == "<div class=\"btn-group\" role=\"group\"><button class=\"btn btn-primary btn-xs dropdown-toggle\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_success_severity_xsmall_split_dropup():
    assert(str(ButtonDropdown("text", size="xs", severity="success", split=True, dropup=True)) == "<div class=\"btn-group dropup\" role=\"group\"><button class=\"btn btn-success btn-xs\">text</button><button class=\"btn btn-success btn-xs dropdown-toggle\" data-toggle=\"dropdown\"><span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_warning_severity_split():
    assert(str(ButtonDropdown("text", severity="warning", split=True)) == "<div class=\"btn-group\" role=\"group\"><button class=\"btn btn-warning\">text</button><button class=\"btn btn-warning dropdown-toggle\" data-toggle=\"dropdown\"><span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_custom_class_ident_and_style():
    assert(str(ButtonDropdown("text", severity="warning", split=True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<div id=\"123-button-dropdown\" class=\"btn-group\" role=\"group\" style=\"font-size:0.9em;\"><button id=\"123\" class=\"btn btn-warning abclass\" style=\"font-size:0.9em;\">text</button><button class=\"btn btn-warning abclass dropdown-toggle\" data-toggle=\"dropdown\"><span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")
