from random import randint

#assume data is a array of bytes
def mutate_jpeg(data, n):
	new_data = []
	size = len(data)
	jpeg_byte_flip(data, new_data, 0, 0,n, size)

	return new_data

def jpeg_byte_flip(data, l, index, count, max_level_recursion, size):

	if count == max_level_recursion:
		return


	byte = data[index]
	lol = byte
	byte = int(byte) ^ 0xff

	
	new = data[0:index] + byte.to_bytes(1, "little") + data[index + 1:]

	l.append(new)



	new_index = randint(0, size)
	#print(f"new_index = {new_index}, index = {index}, old_byte = {lol}, new = {byte}")
	


	jpeg_byte_flip(new, l, new_index, count + 1, max_level_recursion, size)
	jpeg_byte_flip(data, l, new_index, count + 1, max_level_recursion, size)


if __name__ == "__main__":

	f = open("Grosser_Panda.JPG", "rb")
	data = f.read()
	temp = data
	mutated_input = mutate_jpeg(temp, 10) # generate 2 ^ 10 new inputs

	for i in mutated_input:
		print(i == data)

'''
time

real	0m5.201s
user	0m1.212s
sys	0m3.618s

'''