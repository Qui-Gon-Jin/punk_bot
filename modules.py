import random

#check for modifiers
def modificator_check(self):
	if "+" in self.roll[-1] or "-" in self.roll[-1]:
		self.modificator = int(self.roll[-1])
		del self.roll[-1]
	if "*" in self.roll[-1]:
		self.multiply = int(self.roll[-1][1:])
		self.modificator = self.roll[-1]
		del self.roll[-1]
	if "/" in self.roll[-1]:
		self.divide = int(self.roll[-1][1:])
		self.modificator = self.roll[-1]
		del self.roll[-1]

#modificator module
def modificator(self):
	self.throw_result = int(self.throw_result)
	if self.multiply == 1 and self.divide == 1:
		self.throw_result = self.throw_result + self.modificator
	if not self.multiply == 1:
		self.throw_result = self.throw_result * self.multiply
	if not self.divide == 1:
		self.throw_result = self.throw_result / self.divide

#output module
def output(self):
	self.throw_result = int(self.throw_result)
	#bottom cap for result <=0
	if self.throw_result <= 0:
		self.throw_result = 1

	output = (self.author + "\n" + "Result: " + str(self.throw_result) + "\nValues: " + str(self.roll) + "\nSuccess: " + self.success + "\nModificator: " + str(self.modificator))
	return("```" + output + "```")

def help():
	help_file = "help.txt"
	with open(help_file) as help:
		content = help.read()
	return(content)