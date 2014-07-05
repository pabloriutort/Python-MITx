def howMany(aDict):
	'''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
	res = 0
	for key in aDict.keys():
		res += len(aDict[key])
	return res
