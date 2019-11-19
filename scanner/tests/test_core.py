from scanner import core
from unittest import TestCase


class TestCore(TestCase):

    def test_ocrProcessing(self):
        self.assertEqual("A Python Approach to Character\nRecognition",
                         core.ocrProcessing('scanner\\tests\\resources\\test_image.png'))
