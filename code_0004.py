# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

def lowestPosInt(numbers):
  N = len(numbers)
  for i in range(N):
    num = numbers[i]
    if(num <= 0 or num > N):
      pass
    while num != numbers[num - 1]:
      new_num = numbers[num - 1]
      numbers[num - 1] = num
      num = new_num
      if(num <= 0 or num > N):
        break
      
  for i in range(N):
    if(numbers[i] != i + 1):
      return i+1
  
  return N + 1



sample1 = [3,4,-1,1]
should_be = 2
assert lowestPosInt(sample1) == should_be

sample2 = [3,2,1]
should_be2 = 4
assert lowestPosInt(sample2) == should_be2

print('Success!')