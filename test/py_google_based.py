import unittest

from v2x.tools import PyTranslator, GoogleTranslator

test_samples = [
    "Bạn có thể cho tôi một câu chuyện?",
    "Tôi muốn biết thêm về nghệ thuật.",
    "Bạn có thể cho tôi một bài thơ?",
    "Tôi muốn tìm hiểu về công nghệ.",
    "Bạn có thể cho tôi một bài hát?",
]

class TestPyTranslate(unittest.TestCase):
    def setUp(self):
        self.translator = PyTranslator(auto_clean=True)

    def test_sample(self):
        data = test_samples[0]
        result = self.translator.run(text=data)
        self.assertIsInstance(result, str)

    def test_samples(self):
        for data in test_samples:
            result = self.translator.run(text=data)
            self.assertIsInstance(result, str)

class TestGoogleTranslate(unittest.TestCase):
    def setUp(self):
        self.translator = GoogleTranslator(auto_clean=True)

    def test_sample(self):
        data = test_samples[0]
        result = self.translator.run(text=data)
        self.assertIsInstance(result, str)

    def test_samples(self):
        for data in test_samples:
            result = self.translator.run(text=data)
            self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
