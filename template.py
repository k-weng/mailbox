def get_fields(message):
	fields = []
	i = 0
	while i < len(message):
		if message[i] == '[':
			j = i
			while message[j] != ']':
				j += 1
			field = message[i:j+1]
			if field not in fields:
				fields.append(field)
			i = j + 1
		else:
			i += 1
	return fields