import random

filepath = "neural.txt"

layer_size = [4, 10, 10, 1]

content = ""

def randomFloat(start, end):
	return random.random() * (end - start) + start
	
content += "{:d}\n".format(len(layer_size))
	
for size in layer_size:
	content += str(size) + " "
content += "\n\n"

for index in range(1, len(layer_size)):
	for row in range(0, layer_size[index - 1]):
		for col in range(0, layer_size[index]):
			value = randomFloat(-1, 1)
			content += "{:.2f} ".format(value)
		content += "\n"
	content += "\n"
	
	for col in range(0, layer_size[index]):
		value = randomFloat(-1, 1)
		content += "{:.2f} ".format(value)
	
	content += "\n\n"
	
file = open(filepath, "w")
file.write(content)

print("finished")