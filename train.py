import neural
import scanner
import tensorflow as tf

input_path = "input.txt"
output_path = "output.txt"
neural_path = "neural.txt"

############################################################################################

neural_old = neural.Neural()
neural_old.readFromFile(neural_path)

layer_num = neural_old.layer_num
layer_size = neural_old.layer_size
input_size = layer_size[0]
output_size = layer_size[layer_num - 1]
		
print("neural old:\n\n{0}".format(neural_old.toString()))
	
############################################################################################

neural_new = neural.Neural()
neural_new.init(layer_size)
	
def addLayer(index, input, layer, af=None):
	layer_new = neural.Layer()
	layer_new.weight = tf.Variable(layer.weight)
	layer_new.base = tf.Variable(layer.base)
	neural_new.layers[index] = layer_new
	
	output = tf.matmul(input, layer_new.weight) + layer_new.base
	if af is None:
		pass
	else:
		output = af(output)
		
	return output
	
input_data = tf.placeholder(tf.float32, shape=[1, input_size])
output_data = tf.placeholder(tf.float32, shape=[1, output_size])

temp_data = input_data
for i in range(layer_num - 1):
	af = tf.nn.tanh
	temp_data = addLayer(i, temp_data, neural_old.layers[i], af)
	
loss = tf.reduce_mean(tf.reduce_sum(tf.square(output_data - temp_data)))
opti = tf.train.GradientDescentOptimizer(0.1)
train = opti.minimize(loss)

sess = tf.Session()

init = tf.global_variables_initializer()
sess.run(init)
	
############################################################################################

input_scan = scanner.FileScanner(input_path)
output_scan = scanner.FileScanner(output_path)

count = 0

while input_scan.hasNextFloat():
	count += 1
	print("---------------------------------------------")
	print("train", count, "\n")

	inputs = [[]]
	for col in range(input_size):
		value = input_scan.nextFloat()
		inputs[0].append(value)
		
	print("input", inputs, "\n")
		
	outputs = [[]]
	for col in range(output_size):
		value = output_scan.nextFloat()
		outputs[0].append(value)
		
	print("output", outputs, "\n")
		
	feed_dict = {input_data: inputs, output_data: outputs}
	sess.run(train, feed_dict=feed_dict)
	
	result = sess.run(temp_data, feed_dict=feed_dict)
	print("temp_data", result, "\n")
	
	neural_file = open(neural_path, "w")
	neural_file.write("{:d}\n".format(layer_num))
	
	for size in layer_size:
		neural_file.write("{:d} ".format(size))
	neural_file.write("\n\n")
	
	for i in range(layer_num - 1):
		layer = neural_new.layers[i]
		weight = sess.run(layer.weight)
		base = sess.run(layer.base)
		
		for row in weight:
			for value in row:
				neural_file.write("{:.4f} ".format(value))
			neural_file.write("\n")
		neural_file.write("\n")
		
		for row in base:
			for value in row:
				neural_file.write("{:.4f} ".format(value))
			neural_file.write("\n")
		neural_file.write("\n")
		
	neural_file.close()
