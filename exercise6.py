#Author:Wulei
#DATE:2025/3/14
#Outprint the factorial of the number you give but use for loop
#enter a number
a = int(input("Enter the number: "))
b = 1
c = 1
for b in range (1,a+1):
	c = c*b
	b = b + 1
#print out the factorial pf the number
print(c)
