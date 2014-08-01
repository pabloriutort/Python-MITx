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
