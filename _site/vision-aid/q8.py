#i am starting loop
while True:
 try:
  #first input for first number
  x=input('enter first number')
  #second input for second number
  y=input('enter second number')
  x1=float(x)
  y1=float(y)
  break
 except:
  print("please enter numeric value")
  continue
#now it will compare for it is divisible or not
if x1%y1==0:
 print(x1," is divisible by ",y1)
else:
 print(x1," is not divisible by ",y1)
