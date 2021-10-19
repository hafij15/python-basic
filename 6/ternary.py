# a, b = 10, 20
# if a<b: 
#     min = a
# else: 
#     min = b 
# print (min)

"""
response = "y"

while response =="y":
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    if first_num < second_num : 
        min = first_num
    else: 
        min = second_num
    print("The minimum number is : "+str(min))
    response = input("Do you want to continue another process? (y/n) : ")
    
"""

"""
name = ""

default_name = name if name != "" else "Guest"
print (default_name)

"""


response = "y"
while response =="y":
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    
    min = first_num if first_num < second_num else second_num
    print("The minimum number is : "+str(min))
    response = input("Do you want to continue another process? (y/n) : ")
