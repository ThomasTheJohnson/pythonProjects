import gameParameters

#starts a new game objects
newGame = gameParameters.Parameters()
#calls the initWord method to choose a random phrase for the game
newGame.initWord()
#initializes two data structures to keep track of the game entries
inputTable = {}
answerList = []

#makes the list as long as the phrase that was previously initalized
for letters in newGame.word:
    answerList.append("")

#The main game engine
while (not newGame.solved):

    #prints the hangPerson depending on the incorrectGuesses
    if(newGame.getGuesses() == 1):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "                ||\n"
        "                ||\n"
        "                ||\n"
        " _______________||_______\n")
    elif(newGame.getGuesses() == 2):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "  O             ||\n"
        "                ||\n"
        "                ||\n"
        " _______________||_______\n")
    elif(newGame.getGuesses() == 3):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "  O             ||\n"
        "  |             ||\n"
        "                ||\n"
        " _______________||_______\n")
    elif(newGame.getGuesses() == 4):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "  O             ||\n"
        "  |             ||\n"
        " /              ||\n"
        " _______________||_______\n")
    elif(newGame.getGuesses() == 5):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "  O             ||\n"
        "  |             ||\n"
        " / \            ||\n"
        " _______________||_______\n")
    elif(newGame.getGuesses() == 6):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "  O             ||\n"
        "  |\            ||\n"
        " / \            ||\n"
        " _______________||_______\n")
    elif(newGame.getGuesses() == 7):
        print(
        "  /-------------||\n"
        "  |             ||\n"
        "  |             ||\n"
        "  O             ||\n"
        " /|\            ||\n"
        " / \            ||\n"
        " _______________||_______\n")
    else:
        print(
        "  /-------------||\n"
        "                ||\n"
        "                ||\n"
        "                ||\n"
        "                ||\n"
        "                ||\n"
        " _______________||_______\n")

    #This block prints the letters that are in the solution so far.
    print "Solution so far:"
    for letters in answerList:
        print letters,

    #This block prints the letters that have been guessed so far.
    print "\nLetters you have guessed so far:"
    for keys in inputTable:
        print keys,

    #Takes an input from the command line makes it lower case to match the word answers
    userInput = raw_input("\nGuess a letter or phrase!\n")
    userInput = userInput.lower()

    #Manages a table of the inputs that have been 'guessed'
    #If a guess has already been guessed, it doesn't count again
    if(userInput not in inputTable):
        newLetter = {userInput: 1}
        inputTable.update(newLetter)
    else:
        print "You have already guessed that letter!"
        continue

    #If the phrase guessed is totally correct then it exits the loops.
    if(userInput == newGame.word):
        newGame.solved = True

    #If the letter exists in the solution it adds it to the solution list.
    elif(userInput in newGame.word):
        print "\n\n"
        print "Correct!"
        for i in range(len(answerList)):
            if(newGame.word[i] == userInput):
                answerList[i] = userInput
    #This is the condition for if the guess is incorrect
    else:
        newGame.incGuess()
        if(newGame.getGuesses() >= 8):
            print(
                "  /-------------||\n"
                "  |             ||\n"
                "  |             ||\n"
                "  |             ||\n"
                "  O             ||\n"
                " /|\            ||\n"
                "_/ \____________||________\n"
                "\   /\n")
            break
        else:
            print "\n\n"
            print "Guess Again!"

#End of the game message
if(not newGame.solved):
    print "You lose! Better luck next time."
else:
    print "You win! That's pretty cool."
