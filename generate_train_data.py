import random

input_path = "input.txt"
output_path = "output.txt"

input_file = open(input_path, "w")
output_file = open(output_path, "w")

for i in range(100):
	array = []

	for i in range(4):
		value = random.random()
		array.append(value)
		
		input_file.write("{:.4f} ".format(value))
		
	input_file.write("\n")
		
	array.sort()
	
	output_file.write("{:.4f} ".format(array[0]))	
	output_file.write("\n")

print("finished")