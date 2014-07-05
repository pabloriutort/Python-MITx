def recurPower(base,exp):
	if exp == 0:
		return 1
	else:
		return base*recurPower(base,exp-1)

base = int(raw_input("base: "))
exp = int(raw_input("exp: "))
print iterPower(base, exp)	
