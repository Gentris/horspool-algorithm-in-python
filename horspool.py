alphabet: list = [
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
	'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
	'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
	'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
	'w', 'x', 'y', 'z', '0', '1', '2', '3',
	'4', '5', '6', '7', '8', '9', ' ', '`',
	'~', '!', '@', '#', '$', '%', '^', '&',
	'*', '(', ')', '-', '_', '=', '+', '[',
	'{', ']', '}', '\\', '|', ';', ':', '\'',
	'"', ',', '<', '.', '>', '/', '?'
]

def generate_pattern_array(pattern: str):
	pattern_array: list = []
	for i in range(0, len(pattern)):
		pattern_array.append(i)

	return pattern_array

def generate_shift_table(pattern: str, alphabet: list) -> list:
	m: int = len(pattern)
	size: int = len(alphabet)
	table: list = []

	for i in range(0, size):
		table.append(m)

	for i in range(0, m - 1):
		position: int = alphabet.index(pattern[i])
		table[position] = m - i - 1

	return table
