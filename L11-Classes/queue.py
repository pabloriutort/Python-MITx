class Queue(object):
	def __init__(self):
		self.vals = []
	
	def insert(self, e):
		self.vals.append(e)

	def remove(self):
		if self.vals == []:
			raise ValueError()
		else:
			element = self.vals[0]
			self.vals.remove(element)
			return (element)
