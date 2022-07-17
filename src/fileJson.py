from random import randint
def byte_flip_int(num, l, index):
	
	if index == 7:
		return num
	i = 0xff
	i <<= index * 4
	l.append(byte_flip_int(num, l, index + 1))
	l.append(byte_flip_int(num ^ i, l, index + 1))


def byte_flip_str(string, l, index):
	if index == len(string):
		return string

	character = string[index]
	ascii_id = ord(character)

	l.append(byte_flip_str(string, l, index + 1))
	
	new = ""
	for i in string:
		if i == character:
			new += chr(ascii_id ^ 0xff)
		else:
			new += i

	l.append(byte_flip_str(new, l, index + 1))



def repeated_parts(string, l, max, length, start, end, count):
	if count == length:
		return string + string[start: end] * randint(0, max)
	l.append(repeated_parts(string, l, max, length, start, end, count + 1))
	l.append(repeated_parts(string, l, max, length, start, end + 1, count + 1))
	l.append(repeated_parts(string, l, max, length, start + 1, end + 1, count + 1))

def repeated_parts_str(element, temp, max_repeat_time):
	length = len(element)
	repeated_parts(element, temp, max_repeat_time, length, 0, 1, 0)





def generate_inputs(data, method, max_repeat_time = 10):
	inputs = []
	for i in data:
		temp = []

		if type(data) == list:
			element = i
		else:
			element = data[i]

		if type(element) == int or type(element) == float:
			if method == "byte_flips":
				byte_flip_int(element, temp, 0)
			elif method == "repeated_parts":
				assert(max_repeat_time != None)
				temp.append(element * randint(0, max_repeat_time))

		elif type(element) == dict or type(element) == list:
			temp = generate_inputs(element, method)
		elif type(element) == str:
			if method == "byte_flips":
				byte_flip_str(element, temp, 0)
			elif method == "repeated_parts":
				assert(max_repeat_time != None)
				repeated_parts_str(element, temp, max_repeat_time)

		new = [i for i in temp if i != None]
		inputs.append(new)
	return inputs


def chose_sample(inputs, data, sample):
	index = 0
	for i in data:
		if type(data) == list:
			element = i
		elif type(data) == dict:
			element = data[i]

		if type(element) == int or type(element) == float or type(element) == str:
			n = inputs[index][randint(0,len(inputs[index]) - 1)]
			if type(data) == list:
				sample.append(n)
			elif type(data) == dict:
				sample[i] = n
			index += 1
			continue

		
		if type(element) == dict:
			if type(data) == list:
				sample.append({})
				chose_sample(inputs[index], element, sample[-1])
			elif type(data) == dict:
				sample[i] = {}
				chose_sample(inputs[index], element, sample[i])
		else:
			if type(data) == list:
				sample.append([])
				chose_sample(inputs[index], element, sample[-1])
			elif type(data) == dict:
				sample[i] = []
				chose_sample(inputs[index], element, sample[i])
		index += 1

def generate_samples_byte_flips(data, n):
	inputs = generate_inputs(data, "byte_flips")
	total_samples = []


	for i in range(n):
		if type(data) == dict:
			sample = {}
		elif type(data) == list:
			sample = []
		chose_sample(inputs, data, sample)
		total_samples.append(sample)

	return total_samples

def generate_samples_repeated_parts(data, n):
	inputs = generate_inputs(data, "repeated_parts")
	total_samples = []


	for i in range(n):
		if type(data) == dict:
			sample = {}
		elif type(data) == list:
			sample = []
		chose_sample(inputs, data, sample)
		total_samples.append(sample)

	return total_samples



if __name__ == "__main__":
	data = {
    	"len": 12,
    	"input": "AAAABBBBCCCC",
    	"more_data": ["a", "bb"]
	}#data from json1.txt

	sample_inputs = generate_samples_byte_flips(data, 100)

	#sample_inputs = generate_samples_repeated_parts(data, 10)
	
	for i in sample_inputs:
		print(i)