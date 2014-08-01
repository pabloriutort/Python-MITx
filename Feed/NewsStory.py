class NewsStory(object):
	def __init__(self,guid,titl,sub,sumry,link):
		self.guid = guid
		self.titl = titl
		self.sub = sub
		self.sumry = sumry
		self.link = link
	def getGuid(self):
		return self.guid
	def getTitle(self):
		return self.titl
	def getSubject(self):
		return self.sub
	def getSummary(self):
		return self.sumry
	def getLink(self):
		return self.link
