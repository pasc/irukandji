from irukandji.mailparser import Message, generate_message

import unittest

test_data = {

        'l0': 'Hi,\n',
        'l0_header': 'On 1/1/2013, John Smith wrote:\n',
        'l1': '> Hey,\n',
        'l1_header': '> On 2/1/2013, Mark Doe said:\n',
        'l1_b': '>\n',
        'l2': '>> Text Text\n',
        }

class TestParse(unittest.TestCase):
    
    def test_simple(self):
        message = ['l0']
        message = ''.join(map(lambda x: test_data[x], message))

        ret = generate_message(message, '', '')
        self.assertTrue(isinstance(ret, Message))

        self.assertEqual([0], map(lambda x: x.level, ret.content))


    def test_simple_reply(self):
        message = ['l0', 'l0_header', 'l1_header', 'l1', 'l1', 'l0']
        message = ''.join(map(lambda x: test_data[x], message))

        ret = generate_message(message, '', '')
        self.assertTrue(isinstance(ret, Message))

        self.assertEqual([0, 1, 0], map(lambda x: x.level, ret.content))

    def test_simple_reply_with_blank(self):
        message = ['l0', 'l0_header', 'l1_header', 'l1', 'l1_b', 'l1', 'l0']
        message = ''.join(map(lambda x: test_data[x], message))

        ret = generate_message(message, '', '')
        self.assertTrue(isinstance(ret, Message))

        print ret.content
        self.assertEqual([0, 1, 1, 0], map(lambda x: x.level, ret.content))


    def test_simple_long(self):
        message = ['l0', 'l0_header', 'l1_header', 'l1', 'l1', 'l2', 'l1', 'l2', 'l0', 'l1', 'l0']
        message = ''.join(map(lambda x: test_data[x], message))

        ret = generate_message(message, '', '')
        self.assertTrue(isinstance(ret, Message))

        self.assertEqual([0, 1, 2, 1, 2, 0, 1, 0], map(lambda x: x.level, ret.content))


