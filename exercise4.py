#Author:Wulei
#DATE:2025/3/14
#Enter your age to check if any discount you are qualified for
#Enter your age
a = input("Enter your age:")
if int(a) <= 19:
#the situation under 19
	print("you are qualified for student discounts!")
elif  55 >int(a) >19:
#the situation between 19 and 55
	print("you are qualified for no age discounts")
else:
#other situation
	print("you are qualified for senior discounts!")
