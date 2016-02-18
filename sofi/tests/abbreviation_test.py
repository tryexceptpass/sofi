from .. import Abbreviation

def test_basic():
    assert(str(Abbreviation()) == "<abbr title=\"\"></abbr>")

def test_text_and_title():
    assert(str(Abbreviation("Title", "text")) == "<abbr title=\"Title\">text</abbr>")

def test_initialism():
    assert(str(Abbreviation("Title", "text", True)) == "<abbr title=\"Title\" class=\"initialism\">text</abbr>")

def test_custom_class_ident_and_style():
    assert(str(Abbreviation("Title", "text", True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<abbr title=\"Title\" id=\"123\" class=\"initialism abclass\" style=\"font-size:0.9em;\">text</abbr>")