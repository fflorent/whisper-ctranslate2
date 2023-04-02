from faster_whisper.transcribe import Segment

class WordsToSegment():

    def __init__(self):
        self.pending_words = []
        
        
    def _get_words(self, words):
        for word in self.pending_words:
            yield word, True

        for word in words:
            yield word, False

    def get_segment(self, words):
        to_remove = set()

        counter = 0
        text = ""
        start = None
        end = None
        segment_words = []
        for word, pending in self._get_words(words):
            print(f"{counter} - {word} - {pending}")
            text += word.word
            segment_words.append(word)
            if counter == 0:
                start = word.start
                
            if pending:
                print(fPending {word}")            
                to_remove.add(word)                
                                                                              
            counter += 1
            
            if counter >= 5:
                end = word.end
                break
            
            
        for word in words:
            if word not in to_remove:
                print(f"Adding {word}")
                self.pending_words.append(word)
                
        return Segment(start, end, text, segment_words)
