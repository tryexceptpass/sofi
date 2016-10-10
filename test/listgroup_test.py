from sofi.ui import ListGroup, ListItem

def test_basic():
    assert(str(ListGroup()) == "<ul class=\"list-group\"></ul>")

def test_linkify_basic():
    assert(str(ListGroup(linkify=True)) == "<div class=\"list-group\"></div>")

def test_additem():
    lg = ListGroup()
    lg.additem(ListItem("ABC"))
    assert(str(lg) == "<ul class=\"list-group\"><li class=\"list-group-item\">ABC</li></ul>")

def test_linkify_additem():
    lg = ListGroup(linkify=True)
    lg.additem(ListItem("ABC"))
    assert(str(lg) == "<div class=\"list-group\"><a class=\"list-group-item\" href=\"#\">ABC</a></div>")

def test_additem_header():
    lg = ListGroup(linkify=True)
    lg.additem(ListItem("ABC"), heading="HEADING")
    assert(str(lg) == "<div class=\"list-group\"><a class=\"list-group-item\" href=\"#\"><h4 class=\"list-group-item-heading\">HEADING</h4><p class=\"list-group-item-text\">ABC</p></a></div>")

def test_additem_disabled():
    lg = ListGroup()
    lg.additem(ListItem("ABC"), disabled=True)
    assert(str(lg) == "<ul class=\"list-group\"><li class=\"list-group-item disabled\">ABC</li></ul>")

def test_additem_danger():
    lg = ListGroup()
    lg.additem(ListItem("ABC"), severity="danger")
    assert(str(lg) == "<ul class=\"list-group\"><li class=\"list-group-item list-group-item-danger\">ABC</li></ul>")

def test_additem_success():
    lg = ListGroup(linkify=True)
    lg.additem(ListItem("ABC"), severity="success")
    assert(str(lg) == "<div class=\"list-group\"><a class=\"list-group-item list-group-item-success\" href=\"#\">ABC</a></div>")

def test_additem_info():
    lg = ListGroup()
    lg.additem(ListItem("ABC"), severity="info")
    assert(str(lg) == "<ul class=\"list-group\"><li class=\"list-group-item list-group-item-info\">ABC</li></ul>")

def test_additem_warning():
    lg = ListGroup()
    lg.additem(ListItem("ABC"), severity="warning")
    assert(str(lg) == "<ul class=\"list-group\"><li class=\"list-group-item list-group-item-warning\">ABC</li></ul>")

def test_custom_class_ident_style_and_attrs():
    assert(str(ListGroup(cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<ul id=\"123\" class=\"list-group abclass\" style=\"font-size:0.9em;\"></ul>")

def test_linkify_custom_class_ident_style_and_attrs():
    assert(str(ListGroup(linkify=True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<div id=\"123\" class=\"list-group abclass\" style=\"font-size:0.9em;\"></div>")
