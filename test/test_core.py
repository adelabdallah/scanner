from unittest import TestCase

from scanner import core

class TestCore(TestCase):

    def test_ocr_processing(self):
        self.assertEqual("A Python Approach to Character Recognition", core.ocr_processing('./resources/test_image.png'))