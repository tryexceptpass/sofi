from sofi.ui import FontAwesomeIcon

def test_basic():
    assert(str(FontAwesomeIcon()) == "<i class=\"fa\"></i>")

def test_name():
    assert(str(FontAwesomeIcon("home")) == "<i class=\"fa fa-home\"></i>")

def test_size():
    assert(str(FontAwesomeIcon("home", size="2x")) == "<i class=\"fa fa-home fa-2x\"></i>")

def test_fixed():
    assert(str(FontAwesomeIcon("home", fixed=True)) == "<i class=\"fa fa-home fa-fw\"></i>")

def test_spin_animation():
    assert(str(FontAwesomeIcon("spinner", animation="spin")) == "<i class=\"fa fa-spinner fa-spin\"></i>")

def test_pulse_animation():
    assert(str(FontAwesomeIcon("spinner", animation="pulse")) == "<i class=\"fa fa-spinner fa-pulse\"></i>")

def test_rotate():
    assert(str(FontAwesomeIcon("home", rotate="180")) == "<i class=\"fa fa-home fa-rotate-180\"></i>")

def test_flip():
    assert(str(FontAwesomeIcon("home", flip="vertical")) == "<i class=\"fa fa-home fa-flip-vertical\"></i>")

def test_border():
    assert(str(FontAwesomeIcon("home", border=True)) == "<i class=\"fa fa-home fa-border\"></i>")

def test_pull():
    assert(str(FontAwesomeIcon("home", pull="left")) == "<i class=\"fa fa-home fa-pull-left\"></i>")

def test_custom_class_ident_style_and_attrs():
    assert(str(FontAwesomeIcon("home", ident='123', cl="testing", style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<i id=\"123\" class=\"fa fa-home testing\" style=\"font-size:0.9em;\" data-test=\"abc\"></i>")
