from faster_whisper.transcribe import Segment

class WordsToSegment():

    def __init__(self):
        self.pending_words = []
        self.max_words = 5
        
    def _get_words(self):
        while len(self.pending_words) > 0:
            yield self.pending_words.pop(0), True
            
    def get_segments(self, segments):
        for segment in segments:
            yield self.get_segment(segment.words)

        pending = len(self.pending_words) 
        groups = (int)(pending / self.max_words)
        for group in range(groups):
            idx = 5 * group
            yield self.get_segment(self.pending_words[idx : idx + self.max_words], False)

        left = pending - (groups * self.max_words)
        if left > 0:
            yield self.get_segment(segment.words[groups * self.max_words:], False)

    def get_segment(self, words, save = True):
        if save:
            self.pending_words += words

        counter = 0
        text = ""
        start = None
        end = None
        segment_words = []
        for word, pending in self._get_words():
#            print(f"{counter} - {word} - {pending}")
            text += word.word
            end = word.end            
            segment_words.append(word)
            if counter == 0:
                start = word.start
                
            counter += 1
            
            if counter >= self.max_words:
                break
            
        return Segment(start, end, text, segment_words)
