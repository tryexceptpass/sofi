from sofi.ui import ButtonGroup

def test_basic():
    assert(str(ButtonGroup()) == "<div class=\"btn-group\" role=\"group\"></div>")

def test_size_large():
    assert(str(ButtonGroup(size='large')) == "<div class=\"btn-group btn-group-lg\" role=\"group\"></div>")

def test_size_small():
    assert(str(ButtonGroup(size='small')) == "<div class=\"btn-group btn-group-sm\" role=\"group\"></div>")

def test_size_xsmall():
    assert(str(ButtonGroup(vertical=True, size='xsmall')) == "<div class=\"btn-group btn-group-vertical btn-group-xs\" role=\"group\"></div>")

def test_justified():
    assert(str(ButtonGroup(justified=True)) == "<div class=\"btn-group btn-group-justified\" role=\"group\"></div>")

def test_custom_class_ident_and_style():
    assert(str(ButtonGroup(justified=True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<div id=\"123\" class=\"btn-group abclass btn-group-justified\" role=\"group\" style=\"font-size:0.9em;\"></div>")
