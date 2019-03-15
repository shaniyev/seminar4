from mytree import Tree


def main():
	t = Tree()
	f = open('words_50.txt', 'r')
	words = []
	for line in f:
		words.append(line)

	words.sort()

	for word in words:
		t.insert(word)

	t.insert('Hello')

	print(t.min_value()[:-1])
	print(t.max_value()[:-1])
	print(t.length())

	t.delete('Hello')
	print(t.length())

if __name__ == '__main__':
	main()