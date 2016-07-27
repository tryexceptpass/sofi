from .. import UnorderedList

def test_basic():
    assert(str(UnorderedList()) == "<ul></ul>")

def test_text():
    assert(str(UnorderedList("text")) == "<ul>text</ul>")

def test_unstyled():
    assert(str(UnorderedList("text", True)) == "<ul class=\"list-unstyled\">text</ul>")

def test_inline():
    assert(str(UnorderedList("text", inline=True)) == "<ul class=\"list-inline\">text</ul>")

def test_custom_class_ident_and_style():
    assert(str(UnorderedList("text", True, cl='abclass', ident='123', style="font-size:0.9em;"))
           == "<ul id=\"123\" class=\"list-unstyled abclass\" style=\"font-size:0.9em;\">text</ul>")