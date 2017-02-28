import gameParameters

newGame = gameParameters.Parameters()
newGame.initWord()
inputTable = {}
answerList = []
for letters in newGame.word:
    answerList.append("")

print "For testing purposes, the answer is %s" %newGame.word
#The main game engine
while (not newGame.solved):
    print answerList
    print "So far you have guessed:"
    for keys in inputTable:
        print keys,
    userInput = raw_input("\nGuess a letter or phrase!\n")
    userInput = userInput.lower()

    if(userInput not in inputTable):
        newLetter = {userInput: 1}
        inputTable.update(newLetter)
    else:
        print "You have already guessed that letter!"
        continue

    if(userInput == newGame.word):
        newGame.solved = True

    elif(userInput in newGame.word):
        print "-" * 25
        print "Correct!"
        for i in range(len(answerList)):
            if(newGame.word[i] == userInput):
                answerList[i] = userInput
    else:
        newGame.incGuess()
        if(newGame.getGuesses() >= 8):
            break
        else:
            print "-" * 25
            print "Guess Again!"

if(not newGame.solved):
    print "You lose! Better luck next time."
else:
    print "You win! That's pretty cool."
