from sofi.ui import Well

def test_basic():
    assert(str(Well()) == "<div class=\"well\"></div>")

def test_text():
    assert(str(Well("text")) == "<div class=\"well\">text</div>")

def test_small_size():
    assert(str(Well("text",size="small")) == "<div class=\"well well-sm\">text</div>")

def test_large_size():
    assert(str(Well("text",size="lg")) == "<div class=\"well well-lg\">text</div>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Well("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<div id=\"123\" class=\"well abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</div>")
