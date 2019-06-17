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
