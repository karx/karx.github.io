while True:
     #error handling for checking user input 
 try:
  #i will create three variable for taking input from user
  d=input('enter day ')
  m=input('enter month in number')
  y=input('enter year in number')
  #convert in number
  dd=int(d)
  mm=int(m)
  yy=int(y)
  break
 except:
 #for rong input 
  print("invalid input enter numeric values")
  continue
#below code for validating of date 
if dd>0 and dd<32:
 if mm>0 and mm<13:
  if yy>1:
   print("date ",dd,"-",mm,"-",yy)
  else:
   print("invalid year")
 else:
  print("invalid month")
else:
 print("invalid day")
