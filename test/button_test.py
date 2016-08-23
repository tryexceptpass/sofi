from sofi.ui import Button

def test_basic():
    assert(str(Button("text")) == "<button class=\"btn btn-default\">text</button>")

def test_danger_severity_large():
    assert(str(Button("text", "danger", "large")) == "<button class=\"btn btn-danger btn-lg\">text</button>")

def test_info_severity_small():
    assert(str(Button("text", "info", "small")) == "<button class=\"btn btn-info btn-sm\">text</button>")

def test_primary_severity_xsmall():
    assert(str(Button("text", "primary", "xsmall")) == "<button class=\"btn btn-primary btn-xs\">text</button>")

def test_success_severity():
    assert(str(Button("text", "success")) == "<button class=\"btn btn-success\">text</button>")

def test_warning_severity():
    assert(str(Button("text", "warning")) == "<button class=\"btn btn-warning\">text</button>")

def test_custom_class_ident_and_style():
    assert(str(Button("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<button id=\"123\" class=\"btn btn-default abclass\" style=\"font-size:0.9em;\">text</button>")
