import random
import modules

class roll:

	def __init__(self, message, author):
		self.author = author
		self.dice = [0, 10]
		self.roll_result = []
		self.params = []
		self.roll = message.split(" ")
		self.throw_result = 0
		self.throw = 0
		self.modificator = 0
		self.success = ""
		self.multiply = 1
		self.divide = 1
		del self.roll[0]
		modules.modificator_check(self)

	def rolling(self):
		if len(self.roll) >= 2:
			self.roll.append(str(random.randint(1, int(self.dice[1]))))
			for i in self.roll:
				self.throw_result = self.throw_result + int(i)
			if int(self.roll[-1]) == 1:
				self.success = "fail"
			if int(self.roll[-1]) == 10:
				self.success = "crit"

		#roll custom dices
		if "d" in self.roll[0]:
			self.dice[0] = int(self.roll[0].split("d")[0])
			self.dice[1] = int(self.roll[0].split("d")[1])
			del self.roll[0]

			i = 0
			while i < self.dice[0]:
				self.roll.append(random.randint(1, int(self.dice[1])))
				i = i + 1
			for i in self.roll:
				self.throw_result = int(self.throw_result) + int(i)

		#percent roll
		if "%" in self.roll:
			self.throw_result = random.randint(1, 100)
			self.roll[0] = self.throw_result

		#apply modificator
		if not self.modificator == 0:
			 modules.modificator(self)
		
		return(modules.output(self))

	#initiative roll
	def initiative(self):
		self.roll[0] = int(self.roll[0])
		self.roll.append(random.randint(1, 10))
		self.throw_result = self.roll[0] + self.roll[1]

		if not self.modificator == 0:
			modules.modificator(self)
		return(modules.output(self))


