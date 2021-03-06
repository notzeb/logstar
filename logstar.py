import math

default_repeat = 10

def ell(x):
  """compute l(x) = ln(1+x)"""
  return math.log(1+x)

def em(x):
  """compute e(x) = exp(x)-1"""
  return math.exp(x)-1

def lstar(x, repeat = default_repeat):
  """interpolate l*(x) = number of times to apply l before you reach 1"""
  ans = 0
  while x > 1:
    ans = ans+1
    x = ell(x)
  compare = 1
  for i in range(repeat):
    compare = ell(compare)
    x = ell(x)
  #ans = ans + (x-compare)/(compare - ell(compare))
  ans = ans+(2/compare-2/x)
  return ans

def tetrate(x, repeat = default_repeat):
  """inverse function of l*"""
  compare = 1
  for i in range(repeat):
    compare = ell(compare)
  it = math.ceil(x)
  #ans = compare + (x-it)*(compare - ell(compare))
  ans = 2/(2/compare - (x-it))
  for i in range(repeat+it):
    ans = em(ans)
  return ans

def halfexp(x, repeat = default_repeat):
  """function f satisfying f(f(x)) = e(x)"""
  return tetrate(lstar(x, repeat)+0.5, repeat)

def halflog(x, repeat = default_repeat):
  """function f satisfying f(f(x)) = l(x)"""
  return tetrate(lstar(x, repeat)-0.5, repeat)

def fracexp(x, frac, repeat = default_repeat):
  """fractional iteration of e(x)"""
  return tetrate(lstar(x, repeat)+frac, repeat)

