from scanner import core
from unittest import TestCase


class TestCore(TestCase):

    def test_ocrProcessing(self):
        self.assertEqual(['46.13'], core.ocrProcessing('scanner\\tests\\resources\\receipt_2.jpg'))
        self.assertEqual(['81.14'], core.ocrProcessing('scanner\\tests\\resources\\receipt_3.jpg'))
