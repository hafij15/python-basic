age = int(input("What is your age? "))

if age >=18:
    nationalId = input ("Do you have national ID Card?(y/n) ")
    if nationalId == 'y': 
        trade_license = input("Do you have trade license?(y/n)")
        if trade_license =='y': 
            print ("Congrations. You are eligible. ")
        else: 
            print ("You are not eligible. Try again later. Thank you.")
    else: 
        print ("You are not eligible. Try again later. Thank you.")
else:
    print ("You are not eligible. Try again later. Thank you.")