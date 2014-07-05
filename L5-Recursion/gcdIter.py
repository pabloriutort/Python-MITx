def gcdIter(a,b):
	test = min(a,b)
	while test > 1:
		if (a % test == 0) and (b % test == 0):
			break
		else:
			test -=1
	return test

print(gcdIter(2,12))
