# Given an array of integers, return a new array such 
# that each element at index i of the new array is 
# the product of all the numbers in the original array except the one at i.

from functools import reduce

def daily2(numbers):
  total = reduce(lambda x,y: x*y, numbers)
  return [total / x for x in numbers]

def compare(a1, a2):
  for x,y in zip(a1,a2):
    if(x != y): return False
  return True

t1 = daily2([1,2,3,4,5])
assert compare(t1, [120, 60, 40, 30, 24])

t2 =daily2([3,2,1])
assert compare(t2, [2,3,6])

print("Success!")