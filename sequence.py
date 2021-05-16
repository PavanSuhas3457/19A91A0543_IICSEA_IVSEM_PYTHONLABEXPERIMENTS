'''
3.2) Implement a Python Script using for loop that loops
     over a sequence
'''
num = int(input('Enter Your Range:'))
for i in range (1,num+1):
    count = 0
    for j in range(1,num+1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(i,end = ' ')
'''
Output:
Enter Your Range:100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
'''
