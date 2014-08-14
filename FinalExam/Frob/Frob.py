class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    before = atMe.getBefore()
    after = atMe.getAfter()
    if atMe.myName() > newFrob.myName():
         if before == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
         elif before.myName() < newFrob.myName():
            actualInsert(before,newFrob,atMe)
         else:
            insert(before,newFrob)
    else:
        if after == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif after.myName() > newFrob.myName():
            actualInsert(atMe,newFrob,after)
        else:
            insert(after,newFrob)
def actualInsert(f1,f2,f3):
    f1.setAfter(f2)
    f2.setBefore(f1)
    f2.setAfter(f3)
    f3.setBefore(f2)

def findFront(start):
    if start.getBefore().myName() == None:
        return start
    else:
        return findFront(start.getBefore())
