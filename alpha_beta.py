
from sympy import *

# Program to multiply two matrices using list comprehension
 
var('a b c d U V')

# take a 3x3 matrix
A = Matrix([[12, 3], [4, 5]])
 
# take a 3x4 matrix
B = Matrix([["U"], ["V"]])
 
# result will be 3x4
# result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
 
result = A.multiply(B)
 
# for r in result:
#     print(r)
    
print(result)


"""
>>> from sympy import *
>>> var('a c d A B')
(a, c, d, A, B)
>>> A = Matrix([[1, 0], [a, c]])
>>> A
Matrix([
[1, 0],
[a, c]])
>>> B = Matrix([[1, d], [0, 1]])
>>> B
Matrix([
[1, d],
[0, 1]])
>>> M = A.multiply(B)
>>> M
Matrix([
[1,       d],
[a, a*d + c]])
"""