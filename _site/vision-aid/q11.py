while True:
 try:
  #input for taking input from user
  amount=input('enter your per year incam in lak example 250000 lak ')
  #converting in float numeric value
  amount=float(amount)
  break
 except:
  print("invalid input ")
 continue
if amount >0 and amount < 250000:
 print("no tax")
elif amount>250000 and amount <=500000:
 amount1=amount-250000
 amount2=5*amount1/100
 amount3=4*amount2/100
 print("tax",amount2," cess ",amount3,"you have to pay",amount2+amount3)
elif amount > 500000 and amount <= 1000000:
 amount1=amount-250000
 amount2=20*amount1/100
 amount3=4/amount2/100
 print("tax",amount2," cess ",amount3,"you have to pay",amount2+amount3)
elif amount >1000000:
 amount1=amount-250000
 amount2=30*amount1/100
 amount3=4*amount2/100
 print("tax",amount2,"cess ",amount3,"you have to pay",amount2+amount3)
else:
 pass
