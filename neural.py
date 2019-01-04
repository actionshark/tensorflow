import math
import scanner

class Layer:
	def __init__(self):
		self.weight = None
		self.base = None

	def init(self, input_size, output_size):
		self.weight = []
		for row in range(input_size):
			self.weight.append([])
			for col in range(output_size):
				self.weight[row].append(0)
				
		
		self.base = [[]]
		for col in range(output_size):
			self.base[0].append(0)
		
	def toString(self):
		text = ""
	
		for key in self.__dict__:
			text += "{0} : {1}\n".format(key, self.__dict__[key])
			
		return text
		
###############################################################################
		
def tanh(x):
	temp = math.exp(-2 * x)
	return (1 - temp) / (1 + temp)
	
###############################################################################

class Neural:
	def __init__(self):
		self.layer_num = 0
		self.layer_size = []
		self.layers = []
		self.af = tanh
		
	def init(self, layer_size):
		self.layer_num = len(layer_size)
		self.layer_size = layer_size
		self.layers = []
	
		for i in range(self.layer_num - 1):
			input_size = self.layer_size[i]
			output_size = self.layer_size[i + 1]
		
			layer = Layer()
			layer.init(input_size, output_size)
			self.layers.append(layer)
			
	def readFromFile(self, path):
		scan = scanner.FileScanner(path)
		
		layer_num = scan.nextInt()
		layer_size = []
		for i in range(layer_num):
			value = scan.nextInt()
			layer_size.append(value)
		
		self.init(layer_size)
		
		for i in range(layer_num - 1):
			layer = self.layers[i]
			in_size = layer_size[i]
			out_size = layer_size[i + 1]
			
			for row in range(in_size):
				for col in range(out_size):
					layer.weight[row][col] = scan.nextFloat()
					
			for col in range(out_size):
				layer.base[0][col] = scan.nextFloat()
				
		scan.close()
				
	def writeToFile(self, path):
		file = open(path, "w")
		
		file.write("{:d}\n".format(self.layer_num))
		for size in self.layer_size:
			file.write("{:d} ".format(size))
		file.write("\n\n")
		
		for i in range(self.layer_num - 1):
			layer = self.layers[i]
			
			for row in layer.weight:
				for value in row:
					file.write("{:.4f} ".format(value))
				file.write("\n")
			file.write("\n")
					
			for row in layer.base:
				for value in row:
					file.write("{:.4f} ".format(value))
				file.write("\n")
			file.write("\n")
				
		file.close()
		
	def calc(self, inputs):
		for i in range(self.layer_num - 1):
			layer = self.layers[i]
			in_size = self.layer_size[i]
			out_size = self.layer_size[i + 1]
			
			outputs = []
			for col in range(out_size):
				outputs.append(0)
					
			for col in range(out_size):
				for i in range(in_size):
					outputs[col] += inputs[i] * layer.weight[i][col]
						
			for col in range(out_size):
				outputs[col] += layer.base[0][col]
				outputs[col] = self.af(outputs[col])
				
			inputs = outputs

		return inputs
			
	def toString(self):
		text = ""
		
		for i in range(self.layer_num - 1):
			layer = self.layers[i]
			text += "layer {0}:\n{1}\n".format(i, layer.toString());
		
		return text