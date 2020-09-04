# Basic list exercises
# Fill in the definitions for the required functions. The main functions and the testing 
# has been handled, so when you run a program, you will get an output of how many testcases
# passed and how many didn't.

# A. alphanum Score
def alphanum_score(words):
	"""
	The function takes a list of words as its argument.
	Returns a score generated as follows,
		> Start with a net score of 0
		> If the element is a alpha-string, +1
		> If the element is a number-string, -1
	"""

	# Add your code here
	return


# B. Occurences
def occurences(words):
	"""
	The function takes a list of words as its argument.
	Returns a list sorted by the number of times the letter 'a' occurs.
	"""

	# Add your code here
	return


# C. Tuple Merge
def tuple_merge(tuples):
	"""
	The functions takes a list of 2-tuples as its argument.
	Returns a list of the form - 
		[tuples sorted by first element, tuples sorted by second element]
	"""

	# Add your code here
	return


def test(function, input, expected):
	print('\nCASE :', input )
	try:
		assert function(input) == expected
		print('TEST CASE PASSED ! EXPECTED : %s \nOBTAINED : %s' % (expected, function(input)))
	except AssertionError:
		print('TEST CASE FAILED ! EXPECTED : %s \nOBTAINED : %s' % (expected, function(input)))


def main():
	print('\nA. alphanum Score')
	test(alphanum_score, ['abc', '11', 'cde', 'rt', '2', 'word'], 2)
	test(alphanum_score, ['1', '2', 'a', '3', 'b'], -1)
	test(alphanum_score, [], 0)

	print('\nB. Occurences')
	test(occurences, ['apple', 'aardvark', 'empty'], ['empty', 'apple', 'aardvark'])
	test(occurences, ['pple', 'rdvrk', 'empty'], ['pple', 'rdvrk', 'empty'])

	print('\nC. Tuple Merge')
	test(tuple_merge, [(1, 2), (3, 1), (2, 0), (2, 1)], [(1, 2), (2, 0), (2, 1), (3, 1), (2, 0), (3, 1), (2, 1), (1, 2)])
	test(tuple_merge, [(7, 5), (5, 5), (7, 7), (3, 2), (1, 4)], [(1, 4), (3, 2), (5, 5), (7, 5), (7, 7), (3, 2), (1, 4), (7, 5), (5, 5), (7, 7)])
	test(tuple_merge, [(14, 6), (3, 13), (8, 1), (15, 2), (5, 13)], [(3, 13), (5, 13), (8, 1), (14, 6), (15, 2), (8, 1), (15, 2), (14, 6), (3, 13), (5, 13)])


if __name__ == '__main__':
	main()
	