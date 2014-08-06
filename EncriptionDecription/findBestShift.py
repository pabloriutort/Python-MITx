def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    max_realwords_found = 0
    best_shift = 0
    num_valid_words = 0
    i = 0
    while i < 26:
        decode_text = applyShift(text, i)
        decodetext_list = decode_text.split(' ')
        for item in range(len(decodetext_list)):
            if isWord(wordList, decodetext_list[item]) == True:
                num_valid_words += 1
        if num_valid_words > max_realwords_found:
            max_realwords_found = num_valid_words
            best_shift = i
        i += 1
    return best_shift
