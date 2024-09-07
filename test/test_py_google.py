import unittest
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


from v2x.tools import GoogleTranslator

test_samples = [
    "Bạn có thể cho tôi một câu chuyện?",
    "Tôi muốn biết thêm về nghệ thuật.",
    "Bạn có thể cho tôi một bài thơ?",
    "Tôi muốn tìm hiểu về công nghệ.",
    "Bạn có thể cho tôi một bài hát?",
]


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
