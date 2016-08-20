from hypothesis import given, settings, Verbosity
from hypothesis.strategies import text, none

from sofi.ui import Abbreviation

def test_basic():
    assert(str(Abbreviation()) == "<abbr title=\"\"></abbr>")

@given(text(), text())
def test_text_and_title(title, text):
    assert(str(Abbreviation(title, text)) == "<abbr title=\"" + title + "\">" + text + "</abbr>")

def test_initialism():
    assert(str(Abbreviation("Title", "text", True)) == "<abbr title=\"Title\" class=\"initialism\">text</abbr>")

def test_custom_class_ident_style_and_attrs():
    assert(str(Abbreviation("Title", "text", True, cl='abclass', ident='123', style="font-size:0.9em;", attrs={"data-test": 'abc'}))
           == "<abbr title=\"Title\" id=\"123\" class=\"initialism abclass\" style=\"font-size:0.9em;\" data-test=\"abc\">text</abbr>")
