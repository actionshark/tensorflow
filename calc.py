import neural
import sys

neural_path = "neural.txt"

neur = neural.Neural()
neur.readFromFile(neural_path)

inputs = []
for i in range(1, len(sys.argv)):
	value = float(sys.argv[i])
	inputs.append(value)
	
outputs = neur.calc(inputs)

print(outputs)