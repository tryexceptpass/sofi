from sofi.ui import Dropdown

def test_basic():
    assert(str(Dropdown("text")) == "<div class=\"dropdown\"><button class=\"btn btn-default dropdown-toggle\" type=\"button\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_dropup():
    assert(str(Dropdown("text", dropup=True)) == "<div class=\"dropup\"><button class=\"btn btn-default dropdown-toggle\" type=\"button\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_navbaritem():
    assert(str(Dropdown("text", dropup=True, navbaritem=True)) == "<li class=\"dropup\"><a class=\"dropdown-toggle\" href=\"#\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">text <span class=\"caret\"></span></a><ul class=\"dropdown-menu\"></ul></li>")

def test_align_right():
    assert(str(Dropdown("text", align='right', navbaritem=True)) == "<li class=\"dropdown\"><a class=\"dropdown-toggle\" href=\"#\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">text <span class=\"caret\"></span></a><ul class=\"dropdown-menu dropdown-menu-right\"></ul></li>")

def test_custom_class_ident_and_style():
    assert(str(Dropdown("text", cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<div id=\"123-dropdown\" class=\"dropdown abclass\" style=\"font-size:0.9em;\"><button id=\"123\" class=\"btn btn-default dropdown-toggle\" type=\"button\" data-toggle=\"dropdown\">text <span class=\"caret\"></span></button><ul class=\"dropdown-menu\"></ul></div>")

def test_navbaritem_custom_class_ident_and_style():
    assert(str(Dropdown("text", navbaritem=True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<li id=\"123-dropdown\" class=\"dropdown abclass\" style=\"font-size:0.9em;\"><a id=\"123\" class=\"dropdown-toggle\" href=\"#\" role=\"button\" data-toggle=\"dropdown\" aria-haspopup=\"true\" aria-expanded=\"false\">text <span class=\"caret\"></span></a><ul class=\"dropdown-menu\"></ul></li>")
