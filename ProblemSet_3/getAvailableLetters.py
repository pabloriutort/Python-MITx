def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ' '
    str1 = string.ascii_lowercase
    str2=''.join(lettersGuessed)
    result = str1.translate(string.maketrans('',''),str2)
    return result


