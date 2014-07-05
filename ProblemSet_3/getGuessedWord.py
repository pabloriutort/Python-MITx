def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
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


