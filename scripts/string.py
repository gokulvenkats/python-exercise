# Basic string exercises
# Fill in the definitions for the required functions. The main functions and the testing 
# has been handled, so when you run a program, you will get an output of how many testcases
# passed and how many didn't.


# A. Odd Rotation
def odd_rotation(word):
	"""
	The function takes a word as its argument. 
	If the length of the word is even, return the first three characters of the string.
	If the length of the word is odd, return a word formed by a concatenation of the last 2 letters 
	and the first 2 letters of the word.
	"""
	
	# Add your code here
	return 


# B. Flip Case
def flip_case(word):
	"""
	The function takes a word as its argument.
	Return a word that has all lowercase characters swapped to uppercase and vice versa.
	"""

	# Add your code here
	return


# C. And/Or ?
def and_or(word):
	"""
	The function takes a word as its argument.
	If the word starts with 'a', return the index where the substring 'and' appears.
	Otherwise, if the word ends with 'r', return the index where the substring 'or' appears. 
	"""

	# Add your code here
	return


# D. sin + cos
def sincos(number):
	"""
	The function takes a number as its argument.
	Return a string formed by taking the first 5 characters of the result of the expression - 
		sin(number) + cos(number)

	HINT : Look into the math module in more detail
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
	print('\nA. Odd Rotation')
	test(odd_rotation, "apple", "app")
	test(odd_rotation, "orange", "geor")
	test(odd_rotation, "watermelon", "onwa")

	print('\nB. Flip Case')
	test(flip_case, "abcDEfgH", "ABCdeFGh")
	test(flip_case, "xyz", "XYZ")
	test(flip_case, "abcD EFgh IJ", "ABCd efGH ij")

	print('\nC. And/Or ?')
	test(and_or, "ampersand", 6)
	test(and_or, "mortar", 1)

	print('\nD. sin + cos')
	test(sincos, 45, '1.376')
	test(sincos, 23, '-1.37')
	test(sincos, 81, '0.146')


if __name__ == '__main__':
	main()
