##Calculation the value of Pi with a series



x = 0
for i in range(0,int(input())):
  
  if i%2 == 0:
    
    i = 1/(2*i+1)
  elif i%2 ==1:
    i = -1/(2*i+1)
  print(i)
  x+=i
print("")
print(4*x)