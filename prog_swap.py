import sys

def swap():
  
  l = []
  n = int(input("Enter number of elements : "))
  
  for i in range (0,n):
    el= int(input("Enter a number you want: "))
    l.append(el)
    
  a = int(input("Enter 1 number you want to swap: "))
  b = int(input("Enter another number to swap: "))
  
  for i in range (0,n):
    if l[i]==a:
      tmp1=i
    elif l[i]==b:
      tmp2=i
      
  tmp=l[tmp1]
  l[tmp1]=l[tmp2]
  l[tmp2]=tmp
  
  print(l)
  
