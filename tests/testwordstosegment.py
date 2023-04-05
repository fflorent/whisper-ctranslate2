from src.whisper_ctranslate2.wordstosegment import WordsToSegment
from faster_whisper.transcribe import Segment, Word
import unittest


class TestWordsToSegment(unittest.TestCase):
    def test_check_one_line(self):
        MAX_WORDS = 5
        words = []
        text = ""
        for i in range(5):
            word = f"word-{i} "
            text += word
            w = Word(10 + i, 20 + i, word, 1)
            words.append(w)

        segment = Segment(5, 30, text, words, 1, 1)

        new_segments = WordsToSegment(MAX_WORDS).get_segments([segment])
        new_segments = list(new_segments)
        self.assertEquals(1, len(new_segments))
        self.assertEquals(10, new_segments[0].start)
        self.assertEquals(24, new_segments[0].end)
        self.assertEquals("word-0 word-1 word-2 word-3 word-4 ", new_segments[0].text)


if __name__ == "__main__":
    unittest.main()
