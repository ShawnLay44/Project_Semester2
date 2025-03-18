#Add the list of name with Evans and add a new name to become a new list
#Author:Wulei
#Date:2025/3/18
#Create a new list
list1 = ['Lisa','Liam','Leo','Larry','Linda']
a = int(1)
#use for loop to add Evans
for a in range (1,6):
	result = [ name+ 'Evans' for name in list1]
print(result)
#enter a name
b = input("Enter a name:") + "Evans"
result2 = result + [b]
#print out the new list
print (result2)
