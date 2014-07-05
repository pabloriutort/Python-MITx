def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    num = 0
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                num += 1
                break
    return num == len(secretWord)


