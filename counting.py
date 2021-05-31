'''
5.1) Implement a python script to count frequency of
     characters in a given string
'''
string = input('Enter a String:')
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print('The Frequency Count of all Characters in a String is')
print(str(freq))
'''
Output:
Enter a String:Suhas
The Frequency Count of all Characters in a String is
{'S': 1, 'u': 1, 'h': 1, 'a': 1, 's': 1}
'''
