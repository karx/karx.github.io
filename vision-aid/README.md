## Question 1
1. Operators with the same precedence are evaluated in which manner? (1 mark)
K: Left to Right

## Question 2
2. What is the output of print (0.1 + 0.2 == 0.3)? (1 mark)
Answer: false 
K: +1

## Question 3
3. What is the result of the expression 22 % 3 ? (1 mark)
Answer: 1.
K: +1

## Question 4
4. What is the output of “hello”+1+2+3 ? (1 mark)
Answer: TypeError: can only concatenate str (not "int") to str
K: +1

## Question 5
5. What is the average value after the code below is executed? (1 mark)
grade1 = 80
grade2 = 90
average = (grade1 + grade2) / 2
answer: 85.0
K: +1

## Question 6
6. What is the value of the following expression: (1 mark)
float(22//3+3/3)
answer: 8.0
K: +1

## Question 7
For the following questions, remember to use functions, loops, exception handling wherever appropriate. Don't forget to add comments.
7. Write a program that accepts a number and prints its cube and square root (2 marks)
   For e.g. if the number entered is 4, the cube is 64 and the square root is 2.
   Note: Do not use loops
Answer:
```
#import math library 
import math
#input statement for user 
num=input('enter number')
#first i will convert in a number 
num=float(num)
#cube is 
print("cube is ",num*num*num)
#now i will find sqrt
print("square root is ",math.sqrt(num))
```
## Question 8
8. Write a program that accepts 2 numbers and determines whether the first number is divisible by the second. (2 marks)
   For e.g. 
     if the numbers entered are 10 and 2, display 10 is divisible by 2
     If the numbers entered are 11 and 2, print 11 is not divisible by 2.
Answer:
```
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
```
## Question 9
9. Write a program that accepts a string and a letter and returns the number of occurrences of the letter in the 
string. (10 marks)
For example if you entered the string "India is my country" (without quotes) and the letter "i" (without quotes) the program should return 3.
The program should prompt the user repeatedly until he enters "quit". 
Answer:

#function defined for print string letter by letter 
def print_string(str1):
 for lines in str1:
  print(lines)
 return lines
#loop for taking input from user
while True:
#exception handling 
 try:
  str=input('enter string')
  if str=='quit':
   break
#call function for print string letter by letter
  print_string(str)
 except:
  print("return ",3)
 continue
10. Write a program that checks if a date is valid. A date is entered as three integers representing the day, month and year.  (15 marks)

        $ python check-date.py 
        Enter year[1-]:-1
        invalid year
        
        $ python check-date.py 
        Enter year[1-]:20
        Enter month[1-12]: 13
        invalid month
        
        $ python check-date.py 
        Enter year[1-]:2020
        Enter month[1-12]: 2
        Enter day[1-31]:29
        ok
answer:
#i will use loop for checking user enterd numeric value or not
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
11. Write a program to accept user's income as input and calculate taxes using these rules:- (15 marks)
0 - 2.5L => No Tax
2.5L - 5L => 5% of income above 2.5L + 4% of cess
5L - 10L => Tax for 5L + 20% of income above 5L + 4% cess
10L => Tax for 10L + 30% of tax for income above 10L + 4% cess

For example, if users' income is 5L, then 
No tax for first 2.5 L. For reamining 2.5L, 5% tax is 12500.
Now add 4% of cess on 12500 which is 500.
So total tax on 5L will be 13000 
Answer:
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
12. Assume that you deposit 1000 Rs in the bank today and the bank adds 0.06 for every Re after 1 year. Calculate the number of years it will take for your money to become 10,000 and print the amount at the end of each year (50 marks)

For example, after 1 year you will have Re.1060, after 2 years it will be Re.1123.60 in your account.
Answer:
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
