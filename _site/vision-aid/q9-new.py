first=input('enter string')
second=input('enter character which is you want to check how many time came in above string')
count=0
for letters in first:
 if letters==second:
      count=count+1
print(second,"came ",count,"time")

