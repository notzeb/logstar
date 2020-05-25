import math

def ell(x):
  """compute l(x) = ln(1+x)"""
  return math.log(1+x)

def em(x):
  """compute e(x) = exp(x)-1"""
  return math.exp(x)-1

def lstar(x):
  """interpolate l*(x) = number of times to apply l before you reach 1"""
  ans = 0
  while x > 1:
    ans = ans+1
    x = ell(x)
  compare = 1
  for i in range(100):
    compare = ell(compare)
    x = ell(x)
  ans = ans + (x-compare)/(compare - ell(compare))
  return ans

