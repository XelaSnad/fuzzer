from random  import randint
def generate_random_plain_text(string, n):
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
			temp = []
			byte_flips(data, temp, 0, len(data))
			repeated_parts(data, temp, 5, len(data), 0, 1, 0)
			new = [j for j in temp if j != None]

		random.append(new)

	inputs = []
	for i in range(n):
		string = ""
		for i in random:
			random_input = i[randint(0, len(i) - 1)]

			if type(random_input) != str:
				random_input = str(random_input)

			string += random_input
			string += "\n"

		inputs.append(string)

	return inputs



def repeated_parts(string, l, max, length, start, end, count):
	if count == length:
		return string + string[start: end] * randint(1, max)
	l.append(repeated_parts(string, l, max, length, start, end, count + 1))
	l.append(repeated_parts(string, l, max, length, start, end + 1, count + 1))
	l.append(repeated_parts(string, l, max, length, start + 1, end + 1, count + 1))

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
	l = generate_random_plain_text(string, 1000)
	for i in l:
		print(i)
