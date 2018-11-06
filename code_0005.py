# cons(a, b) constructs a pair, 
# and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

def cons(a,b):
  def pair(f):
    return f(a,b)
  return pair

def car(pair):
  return pair(lambda a,b: a)

def cdr(pair):
  return pair(lambda a,b: b)

#test
result = car(cons(3,4))
should = 3
assert result == should

result = cdr(cons(3,4))
should = 4
assert result == should


print('Success!')