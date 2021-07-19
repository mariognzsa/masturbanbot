import random

class Phrases:
    def __init__(self, filename):
        phraseFile = open(filename, "r")
        self.phrases = phraseFile.readlines()
        phraseFile.close()

    def getRandomPhrase(self):
        return random.choice(self.phrases)
