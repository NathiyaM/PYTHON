import re
import csv
class wordcounter:
    def __init__(self,filename):
		self.filename=filename
		self.fo=open(self.filename,'r')
		self.countdict=dict()
		self.items=[]
    def removepunctuation(self):
		remove=re.compile(r'\W+')
		for item in self.fo.readlines():
			word=re.sub(remove,'',item)
			word_lower=word.lower()
			words=word_lower.split(" ")
			self.items.append(self.words)
			
    def findcount(self):
		for i in self.items:
			for self.word in i:
				self.countdict[self.word]=self.countdict.get(self.word,0)+1
    def writecount(self,csvfilename):
		self.csvfilename=csvfilename
		self.columns=['Words','Counts']
		with open(self.csvfilename,'wb') as self.f:
			self.w=csv.writer(self.f,delimiter='\t',lineterminator='\n\n')	
			self.w.writerow(self.columns)
			for self.k,self.v in sorted(self.countdict.items()):
				self.w.writerow([self.k,self.v])
	        self.fo.close()			
wc=wordcounter('red-headed-league.txt')
wc.removepunctuation()
wc.findcount()
wc.writecount('test.csv')
