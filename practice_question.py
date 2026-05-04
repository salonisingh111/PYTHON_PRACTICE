#  — Recursion (Reverse a Number)
# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# print(reverse_number(1234))
# print(reverse_number(120))

# — Recursion (Logic-Based)
# def count_digits(n):
#     if n < 10:
#         return 1
#     return 1 + count_digits(n // 10)

# print(count_digits(12345))
# print(count_digits(7))
# print(count_digits(1000))

# — Lambda + *args + Logic (Harder)
# def count_even(*args):
#     is_even = lambda x:x % 2 == 0
#     count = 0

#     for num in args:
#         if is_even(num):
#             count += 1
#     return count
# print(count_even(1,2,3,4,5,6,7,8,9))

 Q6 — Mixed (Function + *args + Logic)
def sum_even(*args):
    total = 0

    for num in args:
        if num % 2 == 0:
            total += num
    return total
print(sum_even(1,2,3,4,5,6))

