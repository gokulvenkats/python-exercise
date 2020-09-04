"""
Fill in the definitions for the required functions. The main functions and the testing
has been handled, so when you run a program, you will get an output of how many testcases
passed and how many didn't.
"""

# A. dict_with_indexes
def dict_with_indexes(words):
    """
    The function takes a list of words as its argument.
    Returns a dict with the key as the index of the word and value as the word.

    For example, 
    INPUT: ["apple", "ball", "cat", "dog"]
    OUTPUT: {0: "apple", 1: "ball", 2: "cat", 3: "dog"}
    """
    answer = dict()
    words_count = len(words)
    for i in range(words_count):
        answer[i] = words[i]

    return answer


# B. dict_with_lengths
def dict_with_lengths(words):
    """
    The function takes a list of words as its argument.
    Returns a dict with a length as key and a list of words with that length as value.

    For example, 
    INPUT: ["apple", "ball", "cat", "dog", "egg", "fruit"]
    OUTPUT: {3: ["ball", "cat", "dog"], 4: ["ball"], 5: ["apple", "fruit"]}
    """
    answer = dict()
    for word in words:
        key = len(word)
        if key in answer:
            answer[key].append(word)
        else:
            answer[key] = [word]

    return answer


# C. fibonacci
def fibonacci(n):
    """
    The function takes a number `n` as its argument.
    Prints out (NOT RETURN) `n` number of elements of the Fibonacci sequence (starting from 0, 1...)
    You can create additional functions as required.

    For example,
    INPUT: 5
    OUTPUT: 0 1 1 2 3

    INPUT: 10
    OUTPUT: 0 1 1 2 3 5 8 13 21 34
    """
    # You can also use a recursive function if you feel like it's the better solution

    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        print(b)


def test(function, input, expected):
    print('\nCASE :', input )
    try:
        assert function(input) == expected
        print('TEST CASE PASSED ! EXPECTED : %s \nOBTAINED : %s' % (expected, function(input)))
    except AssertionError:
        print('TEST CASE FAILED ! EXPECTED : %s \nOBTAINED : %s' % (expected, function(input)))


def main():
    print('\nA. dict_with_indexes')
    print('====================')
    test(dict_with_indexes, ["apple", "ball", "cat", "dog"], {0: "apple", 1: "ball", 2: "cat", 3: "dog"})
    test(dict_with_indexes, [], {})
    test(dict_with_indexes, ["word1", "word2", "word3"], {0: "word1", 1: "word2", 2: "word3"})

    print('\nB. dict_with_lengths')
    print('====================')
    test(dict_with_lengths, ["apple", "ball", "cat", "dog", "egg", "fruit"], {3: ["cat", "dog", "egg"], 4: ["ball"], 5: ["apple", "fruit"]})
    test(dict_with_indexes, [], {})
    test(dict_with_lengths, ["word1", "word2", "word3"], {5: ["word1", "word2", "word3"]})

    print('\nC. fibonacci')
    print('============')
    print(f'\nn = {5}')
    fibonacci(5)
    print(f'\nn = {10}')
    fibonacci(10)


if __name__ == '__main__':
    main()
