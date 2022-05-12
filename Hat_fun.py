def N(x):
  if x < 0:
    return 0.0
  elif 0 <= x < 1:
    return x
  elif 1 <= x <2:
    return 2-x
  elif x >= 2:
    return 0.0

N(10) 
