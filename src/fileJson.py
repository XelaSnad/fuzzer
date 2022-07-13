import json
import random


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


def generate_inputs(data):
	inputs = []
	for i in data:
		temp = []

		if type(data) == list:
			element = i
		else:
			element = data[i]

		if type(element) == int or type(element) == float:
			byte_flip_int(element, temp, 0)
		elif type(element) == dict or type(element) == list:
			temp = generate_inputs(element)
		elif type(element) == str:
			byte_flip_str(element, temp, 0)

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
			n = inputs[index][random.randint(0,len(inputs[index]) - 1)]
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

if __name__ == "__main__":
	data = {
    	"len": 12,
    	"input": "AAAABBBBCCCC",
    	"more_data": ["a", "bb"]
	}

	inputs = generate_inputs(data)

	if type(data) == dict:
		sample = {}
	elif type(data) == list:
		sample = []
	chose_sample(inputs, data, sample)

	print(sample)	

