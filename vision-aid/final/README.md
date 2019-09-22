Final exam paper - Spring 2019 batch - Python programming.

1. Write a single line script that reverses a given string 
 (2 marks)
answer: rivers.py
```
works +2
```


2. Write a script that accepts a string and prints it 5 times
   For e.g. If the string entered is Python, it should print "PythonPythonPythonPythonPython"
   Do not use loops or multiple print statements.
 (2 marks)
answer: printstatement.py  
```
works +2
```


3. What operator can be used to determine whether a given list has a particular element? 
 (1 mark)
answer: in
```
+1
```

4. What method can be called to add an element to a list?
 (1 mark)
answer: listName.append()

```
+1
```

5. What method can be called to remove an element from a list?
 (1 mark)
answer: list1.pop()
```
+1
```


6. Write a single line script to swap two numbers 
 (1 mark)
answer: swipe.py
```
+1
```


7. Give 2 examples each for mutable and immutable types 
 (2 marks)
answer: mutable example [2,4]
immutable example (45, 21)
```
+2
```


8. Write a program that stores first names and their phone numbers in two lists:-
   ["Tom",  "Jerry",  "Doraemon", "Hattori", "Oggy", "Jack", "Jessie", "James"]
   ["91912", "91232", "91213", "91233", "91999", "91929", "91872", "91234"]
   and returns the requested name's number. 
 (5 marks)
answer: lookup.py

 Output should be like shown below.
 > python lookup.py
 Enter the name to lookup:jerry
 jerry's number is 91232

 > python lookup.py
 Enter the name to lookup:tom
 tom's number is 91912

 > python lookup.py
 Enter the name to lookup:bheem
 Not Found


```
Tested and works
+5
```

9. Write a function that takes a list and a number as argument and returns the number of times it appears in the list. Use this function to find the most frequent number in [1, 1, 2, 1, 3, 1, 6, 2, 1, 2, 1]. 
 (15 marks)
answer: find_frequent.py
 > python find-frequent.py 
 1 is most frequent, appearing 6 times
 
```
The function and logic is good.
Error on Line number 9 at n[0]. Not defined

+2
```



10. Write a program to read the file "names.txt" that contains names of people and outputs unique last names. 
(10 marks)
answer: lastname.py

 > python lastnames.py
 Jain
 Kumar
 Deb
 Mohite
 M
 Shah
 Singh
 Bilal
 Irishnan

```
+7
Tested. 

Fails if second name is not provided.
```

11. Write a function zap() that takes three lists as arguments and returns a list of tuples. 
    Each tuple contains the corresponding element from the list. 
    Assume that all lists are of equal length. 
 (10 marks)
answer: zap.py


 > zap([1, 2, 3], ['a', 'b', 'c'], ['A', 'B', 'C'])
 [(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C'])]
```
TESTED OK +10
```

12. Given a file containing comma separated track of expenses in this format - DATE, EXPENSE, REASON , write a program to find the expenses by month. The output should show the month followed by the amount spent.  
 (50 marks)
answer: expenses.py

 Here is some sample content from the file:- 
 2018-01-21,20,Milk
 2018-01-21,6,Tea
 2018-01-22,50,Bus
 2018-02-21,400,Movie
 2018-02-28,400,Shoes
 2018-03-30,130,Phone Bill
 2018-04-05,10,Coffee
 2018-04-07,110,Grocery
 2018-04-20,80,Notebook
 2019-01-21,21,Milk
 2019-01-21,6,Tea
 2019-01-22,50,Bus
 2019-02-21,500,Movie
 2019-02-28,500,Shoes
 2019-03-30,139,Phone Bill
 2019-04-05,10,Coffee
 2019-04-07,110,Grocery
 2019-04-20,80,Notebook

 > python expenses.py
 2018-01:76
 2018-02:800
 2018-03:130
 2018-04:200
 2019-01:76
 2019-02:1000
 2019-03:139
 2019-04:200

 ```
 +40
Works. Would like to encourage a better way of handling dates in this senario.

Also, the output gives results redundantly
```

