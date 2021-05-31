'''
5.3) Implement a python script to count number of words in a string and reverse each 
     word in a string at the same location.
     Example:
        Input :Honesty is the best policy.
        Output :5 ytsenoH si eht tseb ycilop.
'''
string = input('Enter a String:')
res = len(string.split(' '))
lst = string.split(' ')
new_lst = [i[::-1] for i in lst]
new_string = ' '.join(new_lst)
print(res,end = ' ')
print(new_string)
'''
Output:
Enter a String:Honesty is the Best Policy
5 ytsenoH si eht tseB yciloP
'''

