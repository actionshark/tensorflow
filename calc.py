import math
import neural
import sys

neural_path = "neural.txt"

############################################################################################

def af(x):
	temp = math.exp(-2 * x)
	return (1 - temp) / (1 + temp)

############################################################################################

neur = neural.Neural()
neur.readFromFile(neural_path)

layer_num = neur.layer_num
layer_size = neur.layer_size
	
############################################################################################

inputs = []
for i in range(1, len(sys.argv)):
	value = float(sys.argv[i])
	inputs.append(value)
	
for i in range(layer_num - 1):
	layer = neur.layers[i]
	in_size = layer_size[i]
	out_size = layer_size[i + 1]
	
	outputs = []
	for col in range(out_size):
		outputs.append(0)
			
	for col in range(out_size):
		for i in range(in_size):
			outputs[col] += inputs[i] * layer.weight[i][col]
				
	for col in range(out_size):
		outputs[col] += layer.base[0][col]
		outputs[col] = af(outputs[col])
		
	inputs = outputs

print(inputs)