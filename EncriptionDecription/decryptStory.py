def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    words = loadWords()
    story = getStoryString()
    a = findBestShift(words, story)
    st = applyShift(story, a)
    return st

