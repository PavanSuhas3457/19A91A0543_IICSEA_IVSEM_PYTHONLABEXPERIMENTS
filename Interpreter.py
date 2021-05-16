'''
1.1) Running Instructions in interactive interpreter and a Python Script
'''
>>> num = 20
>>> print(num)
10
>>> type(num)
<class 'int'>
>>> a = 25
>>> b = 30
>>> res = a+b
>>> print(res)
750
>>> str1 = 'Hello Python, Welcome to this World'
>>> type(str1)
<class 'str'>
>>> len(str1)
35
>>> 
#python script to get the bill amount
pa=int(input('Enter the Bill Amount:'))
if pa >= 1000:
    d = 0.1*pa
    print('Discount:',d)
else:
    d = 0.05*pa
    print('Discount:',d)
a = pa-d
print(a)
'''
Output:
Enter the Bill Amount:1500
discount: 150.0
1350.0
'''
