#Reinforcement 1.1 Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise
def is_multiple(n, m):
    return n % m == 0



#R1.2 Write a short Python function, is even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators.
#I used the internet but the whole point was to use bitwise operators
def is_even(k:int):
    return (k & 1 == 0)


#R1.3 Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.
def minmax(data):
    maxm = minm = data[0]
    if len(data) == 1:
        return data
    if len(data) < 1:
        return (0)
    if len(data) > 1:
        for x in data:
            if x > maxm:
                maxm = x
            if x < minm:
                minm = x
    return minm, maxm
        


#R1.4 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the positive integers smaller than n.

def sumsqu(n: int):
    total = 0 
    for i in range(1, n):
        total += i ** 2
    return total



#R1.5 Give a single command that computes the sum from Exercise R-1.4, relying
#on Python’s comprehension syntax and the built-in sum function.
def sumsqu1(n: int):
    total = sum(i**2 for i in range(1, n))
    return total


#R1.6 Write a short Python function that takes a positive integer n and returns
#the sum of the squares of all the odd positive integers smaller than n.
def sumsqu2(n: int):
    total = 0
    for i in range(1, n):
        if i & 1 == 1:
            total += i ** 2
    return total


#R1.7 Give a single command that computes the sum from Exercise R-1.6, relying
#on Python’s comprehension syntax and the built-in sum function.
def sumsqu3(n: int):
    total = sum(i ** 2 for i in range(1, n) if i & 1 == 1)
    return total



#R1.8 Python allows negative integers to be used as indices into a sequence,
#such as a string. If string s has length n, and expression s[k] is used for index
#−n≤k<0, what is the equivalent index j ≥0 such that s[j] references
#the same element?

#(n+k)

#R1.9 What parameters should be sent to the range constructor, to produce a
#range with values 50, 60, 70, 80?

#(50, 81, 10)

#R1.10 What parameters should be sent to the range constructor, to produce a
#range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

#(8, -9, -2 )

#R1.11 Demonstrate how to use Python’s list comprehension syntax to produce
#the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

complist = [2 ** i for i in range(0, 9)]


#R1.12 Python’s random module includes a function choice(data) that returns a
#random element from a non-empty sequence. The random module includes
#a more basic function randrange, with parameterization similar to
#the built-in range function, that return a random choice from the given
#range. Using only the randrange function, implement your own version
#of the choice function.
 
import random 
exdata1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
def mychoice(data):
    n = random.randrange(0, len(data))
    return data[n]

