import abc
class Interestcal():
	__metaclass__ = abc.ABCMeta
	@abc.abstractmethod
	def compcal(self):
		return
	@abc.abstractmethod
	def comput(self):
		return    

class Cical(Interestcal):
    def __init__(self,principal,years,rate):
        self.principal=principal
        self.years=years
        self.rate=rate
    def compcal(self):
        self.cinterest=self.principal*(1+self.rate)**self.years
	def comput(self):
		return self.cinterest

c = Cical(1000,5,6)
c.compcal() 
print c.comput() 
