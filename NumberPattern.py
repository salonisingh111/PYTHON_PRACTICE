''' Create a function that takes a positive integer n and returns numbers from 1 to n separated by spaces using a for loop.
If the input is not an integer, return "Argument must be an integer value."
If the number is less than 1, return "Argument must be an integer greater than 0."'''

def number_pattern(n):

    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    result = ""

    for i in range(1, n + 1):
        result += str(i) + " "

    return result.strip()