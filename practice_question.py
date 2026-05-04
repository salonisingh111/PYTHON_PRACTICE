#  — Recursion (Reverse a Number)
# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# print(reverse_number(1234))
# print(reverse_number(120))

# — Recursion (Logic-Based)
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))
print(count_digits(7))
print(count_digits(1000))
