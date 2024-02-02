def multiply(x: float, y: float) -> float:
    resut = x * y
    return resut


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string: str) -> bool:
    sentence = ""
    for char in string:
        if char.isalnum():
            sentence += char
    return is_palindrome(sentence)


# word = input("Enter a sentence to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


def fibonacci(n: int) -> int:
    """
    Return the fibonacci number for positive `n`.

    :param n: positive value
    :return: the `n` th fibonacci number
    """
    if 0 <= n <=1:
        return n

    n_minus2, n_minus1 = 0, 1

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence(242)
