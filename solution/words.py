import sys

def setup(words):
	new_words = []
	for word in words:
		new_words.append(word.lower())
	words = new_words
	# This could have been done easier with list comprehensions.
	# words = [word.lower() for word in words]
	wordset = set()
	wordcount = dict()
	for word in words:
		prev_size = len(wordset)
		wordset.add(word)
		new_size = len(wordset)
		if new_size > prev_size:
			wordcount[word] = words.count(word)
	return wordset, wordcount

def main():
	if len(sys.argv) == 1 or len(sys.argv) > 2:
		print('FORMAT : python words.py --count|--set')
		sys.exit(0)
	# This could have been done by using exception handlers for IndexError. 
	option = sys.argv[1]
	if option not in ['--count', '--set']:
		print('FORMAT : python words.py --count|--set')
		sys.exit(0)
	try:
		with open('input.txt', 'r') as f:
			text = f.read()
	except Exception:
		print('Rename one of the two files there as input.txt')
	words = text.split()
	wordset, wordcount = setup(words)
	if option == '--set':
		content = " ".join(sorted(list(wordset)))
		with open('output.txt', 'w') as f:
			f.write(content)
	elif option == '--count':
		content = " ".join(sorted(wordcount, key=wordcount.get, reverse=True))
		with open('output.txt', 'w') as f:
			f.write(content)

if __name__ == '__main__':
	main()