from sofi.ui import Image

def test_basic():
    assert(str(Image("default.png")) == "<img src=\"default.png\">")

def test_width_height():
    assert(str(Image("default.png",width="100",height="300")) == "<img src=\"default.png\" width=\"100\" height=\"300\">")

def test_circle_variety():
    assert(str(Image("default.png",variety="circle")) == "<img src=\"default.png\" class=\"img-circle\">")

def test_rounded_variety():
    assert(str(Image("default.png",variety="rounded")) == "<img src=\"default.png\" class=\"img-rounded\">")

def test_thumbnail_variety():
    assert(str(Image("default.png",variety="thumbnail")) == "<img src=\"default.png\" class=\"img-thumbnail\">")

def test_responsive_image():
    assert(str(Image("default.png",responsive=True)) == "<img src=\"default.png\" class=\"img-responsive\">")

def test_custom_class_ident_style_and_attrs():
    assert(str(Image("default.png", ident='123', cl="testing", style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<img src=\"default.png\" id=\"123\" class=\"testing\" style=\"font-size:0.9em;\" data-test=\"abc\">")

