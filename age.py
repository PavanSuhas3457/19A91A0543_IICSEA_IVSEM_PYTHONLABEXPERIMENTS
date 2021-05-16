'''
3.1) Implement a Python Script for checking whether the
     citizen is eligible for vote or not
'''
age = int(input('Enter Your Age:'))
if age>=18:
    print('This Person is Eligible to Vote')
else:
    print('This Person is not Eligible to Vote')
'''
Output:
Enter Your Age:20
This Person is Eligible to Vote

Enter Your Age:17
This Person is not Eligible to Vote
'''
