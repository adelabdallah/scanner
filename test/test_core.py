from unittest import TestCase

from scanner import core

class TestCore(TestCase):

    def test_ocr_processing(self):
        self.assertEqual("A Python Approach to Character\nRecognition", core.ocr_processing('test/resources/test_image.png'))