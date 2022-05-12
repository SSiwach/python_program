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
def Nv(x):
  r = np.where(x<0, 0.0, 0.0)
  r = np.where(0<=x<1,x,r)
  r = np.where(1 <= 2, 2-x,r)
  r = np.where(x>=2,0.0,r)
  return r

Nv(2)
