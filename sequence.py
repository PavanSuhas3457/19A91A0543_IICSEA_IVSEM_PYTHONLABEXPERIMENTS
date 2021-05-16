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
