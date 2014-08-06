import re

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class WordTrigger(Trigger):
	def __init__(self,word):
		self.word = word.lower()

	def isWordIn(self,text):
		return bool(re.findall(r'\b%s\b' % self.word, text, re.IGNORECASE))

class TitleTrigger(WordTrigger):
	def evaluate(self,story):
		return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
	def evaluate(self,story):
		return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
	def evaluate(self,story):
		return self.isWordIn(story.getSummary())

class NotTrigger(Trigger):
	def __init__(self,trigger):
		self.trigger = trigger

	def evaluate(self,story):
		return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
	def __init__(self,trigger1,trigger2):
		self.trigger1 = trigger1
		self.trigger2 = trigger2
	
	def evaluate(self,story):
		return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

class OrTrigger(Trigger):
	def __init__(self,trigger1,trigger2):
		self.trigger1 = trigger1
		self.trigger2 = trigger2

	def evaluate(self,story):
		return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

class PhraseTrigger(Trigger):
	def __init__(self,phrase):
		self.phrase = phrase

	def evaluate(self,story):
		titl = story.getTitle()
		subjct = story.getSubject()
		sumry = story.getSummary()
		return self.phrase in titl or self.phrase in subjct or self.phrase in sumry	

def filterStories(stories,triggerlist):
	newsFiltered = []
	for s in stories:
		for tl in triggerlist:
			if tl.evaluate(s) == True:
				newsFiltered.append(s)
				break #Once found a coincidence, take another story

	return newsFiltered
