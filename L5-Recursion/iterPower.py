def iterPower(base,exp):
	res = 1
	for i in range(exp):
		res *= base
	return res

base = int(raw_input("base: "))
exp = int(raw_input("exp: "))
print iterPower(base, exp)	
