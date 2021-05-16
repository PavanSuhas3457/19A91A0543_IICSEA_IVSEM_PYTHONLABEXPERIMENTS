'''
2.2) Implement a python script add.py that takes 2 numbers
     as command line arguments and perform arithmetic operations
     on them
'''
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print('Sum of the two arguments is',(num1+num2))
print('Difference of the two arguments is',(num1-num2))
print('Product of the two arguments is',(num1*num2))
print('Division of the two arguments is',(num1//num2))
print('Modulus of the two arguments is',(num1%num2))
