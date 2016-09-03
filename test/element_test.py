from sofi.ui import Element


def test_attrs_to_string_shortcut():
    attributes = [
            ('cl', 'class'),
            ('ident', 'id'),
            ]
    e = Element(cl='container', ident='foo')
    should_be = 'class="container" id="foo"'
    assert e._attrs_to_string(attributes) == should_be


def test_attrs_to_string_empty_shortcut():
    attributes = [
            ]
    e = Element()
    should_be = ''
    assert e._attrs_to_string(attributes) == should_be


def test_attrs_to_string_default_arguments():
    e = Element(cl='container', ident='foo')
    should_be = 'class="container" id="foo"'
    assert e._attrs_to_string() == should_be


def test_attrs_to_string_attribute_with_no_value():
    attributes = [
            ('cl', 'class'),
            ('ident', 'id'),
            ('disabled', None),
            ]
    e = Element(cl='container', ident='foo')
    should_be = 'class="container" id="foo" disabled'
    assert e._attrs_to_string(attributes) == should_be


def test_attrs_to_string_with_nonexistent_attribute():
    attributes = [
            ('cl', 'class'),
            ('ident', 'id'),
            ('this_doesnt_exist', 'foo'),
            ]
    e = Element(cl='container', ident='foo')
    should_be = 'class="container" id="foo"'
    assert e._attrs_to_string(attributes) == should_be
