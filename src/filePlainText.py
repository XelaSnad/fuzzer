def generate_random_plain_text(string):
	l = string.split("\n")
	random = []
	for i in l:
		if i == "":
			continue

		try:
			data = int(i)
		except:
			data = i

		new = []





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

		byte_flips(data ^ mask, new, count + 1, max_count)
		byte_flips(data, new, count + 1, max_count)




