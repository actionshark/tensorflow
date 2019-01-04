import math_util
import random

input_path = "input.txt"
output_path = "output.txt"

input_file = open(input_path, "w")
output_file = open(output_path, "w")

for _ in range(30000):
	a = random.randint(0, 15)
	b = random.randint(0, 15)

	for v in math_util.int2bs(a, 4):
		input_file.write("{:d} ".format(v))
		
	for v in math_util.int2bs(b, 4):
		input_file.write("{:d} ".format(v))
		
	input_file.write("\n")

	c = a * b
	
	for v in math_util.int2bs(c, 8):
		output_file.write("{:d} ".format(v))
		
	output_file.write("\n")
	
input_file.close()
output_file.close()

print("finished")