from json import dump, loads

class DATA:
	def __init__(self):
		self.data_file = "data.json"
		self.data = {}

	def load(self):
		try:
			self.data = loads(open(self.data_file, "r").read())
		except:
			print("Data file not found, creating a new one")
			self.save()

	def save(self):
		open(self.data_file, "w").write(dumps(self.data))
