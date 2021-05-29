import random

def wallis(n):
  p=1.0
  for i in range(1,n+1):
    p*=((4)*(i**2))/(((4)*(i**2))-1)
  return p*2
  
def monte_carlo(n):
  x=0.0
  y=0.0
  o=0
  w=0
  for i in range(n):
    x=random.random()
    y=random.random()
    if ((x**2)+(y**2))<=1:
      w+=1
    else:
      o+=1
  p=4*(w/(w+o))
  return p
