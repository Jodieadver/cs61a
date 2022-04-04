# Q1: A plus Abs B
from operator import add, sub
def a_plus_abs_b(a, b):
    if b < 0:
        f = a - b
    else:
        f = a + b
    return f
result = a_plus_abs_b(2, -3)
print("Q1:" , result)

# Q2: Two of Three
# my thought is find the small, and anything that bigger than the smallest number can be used
def two_of_three(a, b, c):
    return a * a + b * b + c * c - min(a, b, c)**2
print("Q2:", two_of_three(1,2,3))

# Q3: Largest Factor
def largest_factor(n):
    # way 1
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list[-2]
#     way 2
    # i = n
    # while i > 0:
    #     i = i - 1
    #     if n % i == 0:
    #         return i
result = largest_factor(15)
print("Q3:" , result)

# Q4: If function vs Statement
# Really funny one
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
result = if_function(3==2, 3+2, 3-2)
print("Q4.1:", result)

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True
def t():
    print(1)
    # return 1
def f():
    print(0)
    # return 1
print("Q4.2.statement:")
with_if_statement()
print("Q4.2.function:")
with_if_function()

# Q5: Hailstone
from operator import mul
def hailstone(n):
    list = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = mul(n, 3) + 1
        list.append(n)
    return list
result  = hailstone(10)
print("Q5:", result, ",length is", len(result))
