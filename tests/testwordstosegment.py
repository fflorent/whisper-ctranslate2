from src.whisper_ctranslate2.wordstosegment import WordsToSegment
from faster_whisper.transcribe import Segment, Word
import unittest


class TestWordsToSegment(unittest.TestCase):
    def test_one_segment(self):
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

    def test_two_segments(self):
        MAX_WORDS = 3
        words = []
        text = ""
        for i in range(7):
            word = f"word-{i} "
            text += word
            w = Word(10 + i, 20 + i, word, 1)
            words.append(w)

        segment = Segment(5, 30, text, words, 1, 1)

        new_segments = WordsToSegment(MAX_WORDS).get_segments([segment])
        new_segments = list(new_segments)

        self.assertEquals(3, len(new_segments))

        self.assertEquals(10, new_segments[0].start)
        self.assertEquals(22, new_segments[0].end)
        self.assertEquals("word-0 word-1 word-2 ", new_segments[0].text)

        self.assertEquals(13, new_segments[1].start)
        self.assertEquals(new_segments[1].words[0].start, new_segments[1].start)
        self.assertEquals(25, new_segments[1].end)
        self.assertEquals("word-0 word-1 word-2 ", new_segments[0].text)

        self.assertEquals(16, new_segments[2].start)
        self.assertEquals(new_segments[2].words[0].start, new_segments[2].start)
        self.assertEquals(26, new_segments[2].end)
        self.assertEquals("word-6 ", new_segments[2].text)


if __name__ == "__main__":
    unittest.main()
