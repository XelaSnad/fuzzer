from random import randint
import io
from PIL import Image
#assume data is a array of bytes
def mutate_jpeg(data, n):
	new_data = []
	size = len(data)
	jpeg_byte_flip(data, new_data, 0, 0,n, size)


	magic_bytes = [0xe0, 0xdb, 0xc4, 0xc0, 0xfe, 0xda]
	jpeg_segment_byte_flip(data, new_data, 0, size, magic_bytes)
	return new_data

def jpeg_byte_flip(data, l, index, count, max_level_recursion, size):

	if count == max_level_recursion:
		return


	byte = data[index]
	lol = byte
	byte = int(byte) ^ 0xff

	
	new = data[0:index] + byte.to_bytes(1, "little") + data[index + 1:]

	l.append(new)



	new_index1 = randint(0, size)
	new_index2 = randint(0, size)
	#print(f"new_index = {new_index}, index = {index}, old_byte = {lol}, new = {byte}")
	


	jpeg_byte_flip(new, l, new_index1, count + 1, max_level_recursion, size)
	jpeg_byte_flip(data, l, new_index2, count + 1, max_level_recursion, size)


def bytes_to_jpeg(data):
	return io.BytesIO(data)
	

def jpeg_segment_byte_flip(data, l, index, size, magic_bytes):
	if index == size:
		return

	for i in range(index, size - 3):
		if int(data[i]) == 0xff and int(data[i+1]) in magic_bytes:
			break

	if i == size - 4:
		return


	if int(data[i + 1]) == 0xd9:
		return

	byte_1 = int(data[i + 2])
	byte_2 = int(data[i + 3])

	new_byte1 = byte_1 ^ 0xff
	new_byte2 = byte_2 ^ 0xff



	new_data_1 = data[0:i + 2] + new_byte1.to_bytes(1, "little") + data[i + 3:]

	new_data_2 = data[0:i + 3] + new_byte2.to_bytes(1, "little") + data[i + 4:]

	new_data_3 = data[0:i + 2] + new_byte1.to_bytes(1, "little") + new_byte2.to_bytes(1, "little") + data[i + 4:]

	l.append(new_data_1)
	l.append(new_data_2)
	l.append(new_data_3)

	magic_bytes.remove(int(data[i + 1]))

	jpeg_segment_byte_flip(data, l, index, size, magic_bytes)
	jpeg_segment_byte_flip(new_data_1, l, i, size, magic_bytes)
	jpeg_segment_byte_flip(new_data_2, l, i, size, magic_bytes)
	jpeg_segment_byte_flip(new_data_3, l, i, size, magic_bytes)




if __name__ == "__main__":

	f = open("Grosser_Panda.JPG", "rb")
	data = f.read()
	temp = data
	mutated_input = mutate_jpeg(temp, 10) # generate 2 ^ 10 new inputs
	images = []
	for i in mutated_input:
		img = bytes_to_jpeg(i)
		images.append(img)

		try:
			file = Image.open(img)
			print("image size= ", file.size)
		except:
			print("except")