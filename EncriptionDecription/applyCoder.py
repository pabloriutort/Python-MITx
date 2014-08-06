def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    result = ''
    L = string.ascii_lowercase
    U = string.ascii_uppercase
   
    for i in range(len(text)):
        if (text[i] not in L) and (text[i] not in U):
            result += text[i]
        else:
            result += coder[text[i]]
   
    return result
