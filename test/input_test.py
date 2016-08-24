import pytest

from sofi.ui import Input

def test_basic_text():
    assert(str(Input('text')) == "<input type=\"text\" class=\"form-control\"></input>")

def test_unknown_inputtype():
    with pytest.raises(ValueError) as err:
        Input('abc')
    assert('abc' in str(err.value))

def test_inputtype_missing():
    with pytest.raises(TypeError):
        Input()

def test_readonly_placeholder():
    assert(str(Input('email', readonly=True, placeholder="abc")) == "<input type=\"email\" class=\"form-control\" placeholder=\"abc\" readonly></input>")

def test_size_large():
    assert(str(Input('password', size="large")) == "<input type=\"password\" class=\"form-control input-lg\"></input>")

def test_size_small():
    assert(str(Input('color', size="small")) == "<input type=\"color\" class=\"form-control input-sm\"></input>")

def test_help_text():
    assert(str(Input('text', helptext="help me")) == "<input type=\"text\" class=\"form-control\" aria-describedby=\"helpBlock\"></input><span id=\"helpBlock\" class=\"help-block\">help me</span>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Input("text", cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<input type=\"text\" id=\"123\" class=\"form-control abclass\" style=\"font-size:0.9em;\" data-test=\"abc\"></input>")
