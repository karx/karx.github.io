y=1
z=0
#loop will be start below
while True:
 try:
  #input for enter deposit amount 
  x=input('enter deposit amount')
  x=float(x)
  break
 except:
  print("invalid input")
  continue
while x<=10000:
 z=x*0.06
 x=x+z
 print("year - ",y," abalance in your account - ",x)
 y=y+1
print("total year - ",y," balance in your account - ",x)
