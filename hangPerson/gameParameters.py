import random

#This class holds the paramters for the game
class Parameters:


#    There are 4 differnt parameters for the game so far.
#wordCode helps choose the random phrase for the game
#guesses is the total number of guesses made so far.
#totalGuesses is the total number of guesses possible
#word is the word or phrase used by the game

    def __init__(self):
        self.wordCode = random.randint(1,6)
        self.incorrectGuesses = 0
        self.totalGuesses = 8
        self.word = ""
        self.solved = False

#Uses a randomly generated number to change the phrase for the game.
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

        self.word = self.word.lower()

#Adds to the total number of guesses
    def incGuess(self):
        self.incorrectGuesses += 1

#Gets the number of guesses that have been made so far
    def getGuesses(self):
        return self.incorrectGuesses

#returns the phrase that is being used this game.
    def getWord(self):
        return self.word
