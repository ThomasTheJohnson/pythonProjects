import gameParameters

newGame = gameParameters.Parameters()
newGame.initWord()
wordList = []

#Generating a list form of the word being guessed
for letters in newGame.word:
    if(letters.isspace()):
        wordList.append("space")
    else:
        wordList.append("")
tuple(wordList)

print "For testing purposes, the answer is %s" %newGame.word
#The main game engine
while (not newGame.solved and newGame.getGuesses() <= 8):
    userInput = raw_input("Guess a letter or phrase!\n")
    userInput = userInput.lower()

    if(userInput == newGame.word):
        newGame.solved = True

    elif(userInput in newGame.word):
        print "Correct!"

    else:
        print "Guess Again!"
        newGame.incGuess()

if(not newGame.solved):
    print "You lose! Better luck next time."
else:
    print "You win! That's pretty cool."
