
print("Hello Functions")


#Chapter One of Functional Programming by Lott
def sum(seq):
    if len(seq) ==0: return 0
    return seq[0] + sum(seq[1:])
#print(sum([1,2,3]))
#multiplesOf15 = [15, 30, 45, 60, 75, 90]
#print(multiplesOf15[1:])


# Understanding Python comprehensions  - ChatGPT
squares = []
for num in range(10):
    squares.append(num ** 2)
print(squares)

squares_comprehension = [num ** 2 for num in range(10)]
print(squares_comprehension)

# Understanding Generator Expressions in Python
squares_generator = (num ** 2 for num in range(10))
print(list(squares_generator))

# Regular function
def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

#print(add_lambda(1, 2))

#map() function
numbers = [1,2,3,4,5]
squared_numbers = map(lambda x:x**2, numbers)

# https://realpython.com/lessons/mutable-data-structures-lists-dictionaries/
scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': '1815', 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': '1882', 'nobel': False},
    {'name': 'Marie Curie', 'field': 'physics', 'born': '1867', 'nobel': True},
    {'name': 'Tu Youyou', 'field': 'chemistry', 'born': '1930', 'nobel': True},
    {'name': 'Ada Yonath', 'field': 'chemistry', 'born': '1939', 'nobel': True},
    {'name': 'Vera Rubin', 'field': 'astronomy', 'born': '1928', 'nobel': False},
    {'name': 'Sally Ride', 'field': 'physics', 'born': '1951', 'nobel': False}
]

#print(scientists)

import collections

# This is immutable
scientists_collections = collections.namedtuple('scientists_collections', [
'name', 'field', 'born', 'nobel'
])

#print(scientists_collections)

#ada = scientists_collections(name='Ada Lovelace', field='math', born='1815', nobel=False)
#print(ada.born)
ada = scientists_collections(name='Ada Lovelace', field='math', born='1815', nobel=False)
emmy = scientists_collections(name='emmy noether', field='math', born='1882', nobel=False)
marie = scientists_collections(name='Marie Curie', field='Pysics', born='1867', nobel=True)
tu = scientists_collections(name='Tu Youyou', field='chemistry', born='1930', nobel=True)
yonath = scientists_collections(name='Ada Yonath', field='chemistry', born='1939', nobel=True)
vera = scientists_collections(name='Vera Rubin', field='chemistry', born='1928', nobel=False)
sally = scientists_collections(name='Sally Ride', field='pysics', born='1951', nobel=False)

#scientists_list = [ada, emmy, marie, tu, yonath, vera, sally] # NO GOOD - lists are mutable

from pprint import pprint

scientists_tuple = ada, emmy, marie, tu, yonath, vera, sally
#pprint(scientists_tuple)

#print(scientists_tuple[0])


results = filter(lambda x: x.nobel is True, scientists_tuple)
# lambda x: x.field == 'physics' and x.nobel
#print(results)
#print(tuple(results))

#pprint(tuple(results))

#for scientist in results:
#    pprint(scientist.name)

#pprint([x for x in scientists_tuple if x.nobel is True])

pprint(scientists_tuple)

ages_of_scientists = map(lambda x: 2023-int(x.born), scientists_tuple)

pprint(tuple(ages_of_scientists))

from functools import reduce


nums = (1,2,3,4,5,6,7,8)
s=0
for i in nums:
    s += i**2

print(str(s))

print(list(map(lambda h: h**2, nums)))

s = reduce(lambda x, y: x+y, map(lambda h: h**2, nums))
print(str(s))

#Given the tuple of numbers nums
numbersOfMine = (2, 12, 14, 1, 8, 10, 3, 7, 5, 15)

#First - find all numbers greater than 10 (FILTER)

#Second - square them MAP

#third - find the min REDUCE

#Figure out how to chain them together