from sofi.ui import Textarea

def test_basic():
    assert(str(Textarea()) == "<textarea class=\"form-control\"></textarea>")

def test_text():
    assert(str(Textarea("text")) == "<textarea class=\"form-control\">text</textarea>")

def test_rows():
    assert(str(Textarea(rows=5)) == "<textarea class=\"form-control\" rows=\"5\"></textarea>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Textarea("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<textarea id=\"123\" class=\"form-control abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</textarea>")
