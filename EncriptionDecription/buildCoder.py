def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    cipher_key = {s2[i]: (s2[shift:] + s2[:shift])[i] for i in range(26)}
    cipher_key.update({s1[i]: (s1[shift:] + s1[:shift])[i] for i in range(26)})
    return cipher_key
