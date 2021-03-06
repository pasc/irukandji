from irukandji.mailparser import Message

indent_data = [
 (0, 'this has no indent', 'this has no indent'),
 (0, ' this also has no indent', ' this also has no indent'),
 (1, '>this is squished', 'this is squished'),
 (1, '> this is a normal one level', ' this is a normal one level'),
 (1, '> This is a single level where I think a > b', ' This is a single level where I think a > b'),
 (1, 'john> this is also a single level', ' this is also a single level'),
 (2, '>> This is a reply', ' This is a reply'),
 (2, '> > This is also a reply', ' This is also a reply'),
 (2, '> john> this is a second level too', ' this is a second level too'),
 (2, 'mike> john> this is rare', ' this is rare'),
 (2, '>>', ''),
 (3, '>>> This is a reply to a reply', ' This is a reply to a reply'),
 (3, '> >> This went through two different MUAs', ' This went through two different MUAs'),
        ]

def test_indent():
    for indent, text, strip in indent_data:
        yield check_indent, indent, text
        yield check_strip, indent, text, strip

def check_indent(indent, text):
    message = Message()
    assert message.indent_level(text) == indent, message.indent_level(text)

def check_strip(indent, text, strip):
    message = Message()
    assert message.strip_levels(indent, text) == strip, message.strip_levels(indent, text)
