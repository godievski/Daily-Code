# given a list of number and a number K, return whether any two numbers from the list add up to k
def daily1 (numbers, k):
  to_match = {}
  for num in numbers:
    if to_match.get(k - num, False) :
      return True
    else:
      to_match[num]  = True
  return False

      
#Test
assert daily1([15,10,3,7], 17)

assert daily1([15,199,6,6], 12)

assert daily1([1,2,3,4], 9) == False

print("Success!")