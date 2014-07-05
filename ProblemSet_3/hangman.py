def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is ", len(secretWord), " letters long."
    print "----------"
    lettersGuessed = ['']
    guesses = 8
    while (not (isWordGuessed (secretWord,lettersGuessed)) and guesses > 0):
        print "You have ",guesses,"guesses left"
        print "Available letters: "+getAvailableLetters(lettersGuessed)
        l = raw_input("Please guess a letter: ")
        if l in lettersGuessed:
            print "Oops! You've already guessed that letter: " +getGuessedWord(secretWord,lettersGuessed)
        else:
            lettersGuessed.append(l)
            if l in secretWord:
                print "Good guess: "+getGuessedWord(secretWord,lettersGuessed)
            else:
                print "Oops! That letter is not in my word: "+getGuessedWord(secretWord,lettersGuessed)
                guesses -= 1
        print "-----------"
    if guesses == 0:
        print "Sorry, you ran out of guesses, The word was " +secretWord
    else:
        print "Congratulations, you won!"

def getGuessedWord(secretWord, lettersGuessed):
    result= ' '
    found = False
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                result += i
                found = True
        if not found:
            result += ' _'
        found = False
    return result

def isWordGuessed(secretWord, lettersGuessed):
    num = 0
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                num += 1
                break
    return num == len(secretWord)

def getAvailableLetters(lettersGuessed):
    result = ' '
    str1 = string.ascii_lowercase
    str2=''.join(lettersGuessed)
    result = str1.translate(string.maketrans('',''),str2)
    return result
    

