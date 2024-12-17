#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str): 
            self.value = value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        """Returns True if the string ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the string ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the string ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the string."""
        
        import re

        
        sentences = re.split(r'[.?!]', self.value)
        
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)


string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences()) 

