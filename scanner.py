blank_chars = [" ", "\n", "\t"]

def isBlank(char):
	for blank in blank_chars:
		if char == blank:
			return True
	return False

class FileScanner:
	def __init__(self, filepath):
		self.file = open(filepath, "r")
		self.cache = ""
	
	def hasNextLine(self):
		if self.cache == "":
			self.cache = self.file.readline()
			
		return self.cache != ""
		
	def nextLine(self):
		if not self.hasNextLine():
			raise Exception("no next line")
		
		result = self.cache[:-1]
		self.cache = ""
		return result
			
	def hasNextWord(self):
		while self.hasNextLine():
			for char in self.cache:
				if not isBlank(char):
					return True
					
			self.cache = ""
				
		return False
		
	def nextWord(self, remove=True):
		if not self.hasNextWord():
			raise Exception("no next word")
			
		length = len(self.cache)
		start = 0
		end = 0
		
		for index in range(length):
			char = self.cache[index]
			if not isBlank(char):
				start = index
				break
				
		for index in range(start + 1, length):
			char = self.cache[index]
			if isBlank(char):
				end = index
				break
				
		result = self.cache[start:end]
		
		if remove:
			self.cache = self.cache[end:]
		
		return result
		
	def hasNextToken(self, convert):
		if not self.hasNextWord():
			return False
			
		word = self.nextWord(False)
		try:
			convert(word)
			return True
		except:
			return False
			
	def nextToken(self, convert):
		if not self.hasNextToken(convert):
			raise Exception("no next token")
		
		word = self.nextWord()
		return convert(word)
		
	def hasNextInt(self):
		return self.hasNextToken(int)
		
	def nextInt(self):
		return self.nextToken(int)
		
	def hasNextFloat(self):
		return self.hasNextToken(float)
	
	def nextFloat(self):
		return self.nextToken(float)
		
	def close(self):
		self.file.close()