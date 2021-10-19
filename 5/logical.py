# Logical Operator :: and , or, not

name = "Hafijur Rahman"
age  = 30

name_matched = name == "Hafijur Rahman"
age_matched  = age > 25

#print (name_matched)
#print (age_matched)

print (name_matched and age_matched) ###  Both value must be true else false.
print (name_matched or age_matched) ###  Both value must be false else true.

#Truth Table
# Conditon A    Condition B     And         Or
#   True            True        True        True
#   True            False       False       True
#   False           True        False       True
#   False           False       False       False   

print ( not name_matched)