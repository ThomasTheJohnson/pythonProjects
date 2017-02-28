import random

class Parameters:

    def __init__(self):
        self.wordCode = random.randint(1,6)
        self.guesses = 0
        self.totalGuesses = 8
        self.word

    def initWord(self):
        if(self.wordCode == 1):
            self.word = "Pythagoras"
        elif(self.wordCode == 2):
            self.word = "Han Solo on a Tauntaun"
        elif(self.wordCode == 3):
            self.word = "Freaks and Geeks"
        elif(self.wordCode == 4):
            self.word = "Dreaming Green"
        elif(self.wordCode == 5):
            self.word = "National Geographic"
        else:
            self.word = "Puppies and Kittens"

    def incGuess(self):
        self.guesses += 1

    def getGuesses(self):
        return self.guesses

    def getWord(self):
        return self.word
