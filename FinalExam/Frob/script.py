from Frob import *
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

list = []
list.append(andrew)
after = andrew.getAfter()

while after != None:
    list.append(after)
    after = after.getAfter()

print "descendiente"
for i in list:
    print i.myName()

print "\nascendiente"
for i in reversed(list):
    print i.myName()