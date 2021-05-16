'''
1.2) Implement a Python Script to purposefully
     raise Indentation Error and Correct it
'''
num = int(input('Enter a Number:'))
i = 1
while i<num:
print(i)    #Raises an Indentation Error
    i += 1

num = int(input('Enter a Number:'))
i = 1
while i<num:
    print(i)    #Correction of this Indentation Error
    i += 1
'''
Output:
Enter a Number:10
1
2
3
4
5
6
7
8
9
10
'''
