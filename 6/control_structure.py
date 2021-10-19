# What is control structure?
# Some basic code structure which can control our program. 
"""
a, b = 10, 20
c = a + b
d = a - b

results = c*c + d*d
print (results)

"""

# Control structures 1 :: Conditions
# Control Structures 2 :: Loops

# Conditions :: Which block will be execute or which will not depends on decisions. 
# Loops :: Which block of codes will execute repeteadly. 

# Conditions ::  
# IF
# ELIF
# ELSE

# LOOP :: 
# FOR LOOP
# While Loop

#### Even or ODD ####
"""
x = int(input("Enter a number : "))
print(type(x))
if x % 2 == 0 : 
    print("x is even number")
else : 
    print("x is odd number")
"""

"""
class_one   =  8
class_two   =  9
class_three =  10
class_four  =  11
class_five  =  12
#print (class_one)
student_age = int(input("Enter students age : "))
#print(type(student_age))
print ("The student age is : "+ str(student_age))
#print (class_one)
if student_age == 8 :
    print("The student is class one's students")
elif student_age == 9 :
    print("The student is class two's students")
elif student_age == 10 :
    print("The student is class three's students")
elif student_age == 11 :
    print("The student is class four's students")
elif student_age == 12 :
    print("The student is class five's students")
else :
    print("Please contact with the authority")
"""


"""
person1_name = input("Enter the name of first person: ")
person2_name = input("Enter the name of second person: ")

person1_age = int(input("Enter the age of first person: "))
person2_age = int(input("Enter the age of second person: "))


print("The name of first person is: " + person1_name)
print("The name of second person is: " + person2_name)

print("The name of first person age is: " + str(person1_age))
print("The name of second person age is: " + str(person2_age))

if person1_age > person2_age: 
    print (person1_name +" is older than " + person2_name)
elif person1_age < person2_age: 
    print (person1_name +" is youngest than " + person2_name)
else:
    print (person1_name + " and " + person2_name + " is same year's old.")
"""