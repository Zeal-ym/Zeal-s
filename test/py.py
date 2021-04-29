print("The Lucky Number is Between 0 to 100 ")
lucky_number=35
guess=0
while guess != lucky_number :
    guess=int(input("number is :"))
    if guess > 0 and  guess< 100 :
        if guess > lucky_number :
            print("number is smaller than that")
        elif guess < lucky_number :
            print("number is larger than that")
        elif guess == lucky_number :
            print('You are god damn right!!!')
    else :
        print("Did u read the caption clearly fool??")