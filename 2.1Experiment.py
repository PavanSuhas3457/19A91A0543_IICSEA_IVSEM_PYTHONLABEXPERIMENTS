'''
2.1) Implement a Python script to compute distance between
     two points taking inp from the user (Pythagorean Theorem).
'''
import math as m
x1 = int(input('Enter x1:'))
x2 = int(input('Enter x2:'))
y1 = int(input('Enter y1:'))
y2 = int(input('Enter y2:'))
res = (m.sqrt((x2-x1)**2+(y2-y1)**2))
print('The distance between',(x1,y1),'and',(x2,y2),'is',round(res,2))
'''
Output:
Enter x1:4
Enter x2:8
Enter y1:9
Enter y2:6
The distance between (4, 9) and (8, 6) is 5.0
'''
