from sofi.ui import DropdownItem

def test_basic():
    assert(str(DropdownItem()) == "<li></li>")

def test_text():
    assert(str(DropdownItem("text")) == "<li><a href=\"#\">text</a></li>")

def test_disabled():
    assert(str(DropdownItem("text", disabled=True)) == "<li class=\"disabled\"><a href=\"#\">text</a></li>")

def test_header():
    assert(str(DropdownItem("text", header=True)) == "<li class=\"dropdown-header\"><a href=\"#\">text</a></li>")

def test_divider():
    assert(str(DropdownItem(divider=True)) == "<li class=\"divider\"></li>")

def test_custom_class_ident_style_and_attrs():
    assert(str(DropdownItem("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<li id=\"123\" class=\"abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"><a href=\"#\">text</a></li>")
