from src.whisper_ctranslate2.wordstosegment import WordsToSegment
from faster_whisper.transcribe import Segment, Word
import unittest


class TestWordsToSegment(unittest.TestCase):
    def test_check_one_line(self):
        words = []
        text = ""
        for i in range(5):
            word = f"word-{i}"
            text += word
            w = Word(10 + i, 20 + i, word, 1)
            words.append(w)

        segment = Segment(5, 20 + (5 * 10), text, words, 1, 1)

        new_segments = WordsToSegment().get_segments([segment])
        new_segments = [new_segments]
        self.assertEquals(1, len(new_segments))


if __name__ == "__main__":
    unittest.main()
