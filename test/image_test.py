from sofi.ui import Image
import os

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

def test_data_uri():
    img = Image()
    img.datauri(os.path.join(os.path.dirname(__file__), "test.png"))

    src = 'data:image/png;base64,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'

    assert(str(img) == "<img src=\"" + src + "\">")
