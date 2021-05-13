#Finding the value of pi using series LEIBNIZ (1-1/3+1/5-1/7..............)

#By calculating it to the value of 10^8. I was able to get the accuracy up to 6 decimal places


x = 0
for i in range(0,int(input())):
  
  if i%2 == 0:
    i = 1/(2*i+1)
  elif i%2 ==1:
    i = -1/(2*i+1)
  #print(i)
  x+=i
print("")
print(4*x)
