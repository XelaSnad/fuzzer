def generate_random_plain_text(string):
	l = string.split("\n")
	print(l)
	random = []
	for i in l:
		if i == "":
			continue

		new = []
		try:
			data = int(i)
			byte_flips(data, new, 0, 4)
		except:
			data = i
			byte_flips(data, new, 0, len(data))

		random.append(new)

	return random


		





def byte_flips(data, new, count, max_count):
	if count == max_count:
		return


	if type(data) == int:
		mask = 0xf << (count * 4)
		new.append(data ^ mask)
		byte_flips(data ^ mask, new, count + 1, max_count)
		byte_flips(data, new, count + 1, max_count)

	elif type(data) == str:
		if count == len(data):
			return
		char = data[count]
		ascii_id = ord(char)

		new_str = data[0:count] + chr(ascii_id ^ 0xff) + data[count + 1:]

		new.append(new_str)

		byte_flips(data, new, count + 1, max_count)
		byte_flips(new_str, new, count + 1, max_count)




if __name__ == "__main__":

	string = "trivial\n2\n" #plaintext2.txt
	l = generate_random_plain_text(string)
	for i in l:
		print(i)
