import unittest
from mock import Mock

from irukandji.mailformat import format_mail

class TestFormatMail(unittest.TestCase):
    def setUp(self):
        self.mail = Mock()
        self.mail.authors = ['a1', 'a2', 'a3', 'a4']

        self.l1 = Mock()
        self.l1.level = 1

        self.l2 = Mock()
        self.l2.level = 2

        self.l3 = Mock()
        self.l3.level = 3

        self.l4 = Mock()
        self.l4.level = 4

    def test_simple(self):
        self.mail.content = [self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 2)
        self.assertEqual(len(ret.split("</div")), 2)


    def test_simple_multiple(self):
        self.mail.content = [self.l1, self.l1, self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 2)
        self.assertEqual(len(ret.split("</div")), 2)

    def test_single_reply(self):
        self.mail.content = [self.l1, self.l2, self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 3)
        self.assertEqual(len(ret.split("</div")), 3)

    def test_single_reversed_reply(self):
        self.mail.content = [self.l2, self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 3)
        self.assertEqual(len(ret.split("</div")), 3)

    def test_single_dangling(self):
        self.mail.content = [self.l1, self.l2]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 3)
        self.assertEqual(len(ret.split("</div")), 3)

    def test_multi_reply(self):
        self.mail.content = [self.l1, self.l2, self.l3, self.l2, self.l3, self.l2, self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 5)
        self.assertEqual(len(ret.split("</div")), 5)

    def test_multi_reply_double(self):
        self.mail.content = [self.l1, self.l2, self.l3, self.l3, self.l2, self.l2, self.l3, self.l2, self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 5)
        self.assertEqual(len(ret.split("</div")), 5)

    def test_multi_gap_reply(self):
        self.mail.content = [self.l1, self.l2, self.l3, self.l1, self.l3, self.l2, self.l1]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 6)
        self.assertEqual(len(ret.split("</div")), 6)

    def test_multi_gap_reply_dangling(self):
        self.mail.content = [self.l1, self.l2, self.l3, self.l1, self.l3, self.l2]
        ret = format_mail(self.mail)
        self.assertEqual(len(ret.split("<div")), 6)
        self.assertEqual(len(ret.split("</div")), 6)


