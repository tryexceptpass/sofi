from sofi.ui import PageHeader

def test_basic():
    assert(str(PageHeader()) == "<div class=\"page-header\"><h1></h1></div>")

def test_text():
    assert(str(PageHeader("text")) == "<div class=\"page-header\"><h1>text </h1></div>")

def test_text_subtext():
    assert(str(PageHeader("text","subtext")) == "<div class=\"page-header\"><h1>text <small>subtext</small></h1></div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(PageHeader("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"page-header abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"><h1>text </h1></div>")
