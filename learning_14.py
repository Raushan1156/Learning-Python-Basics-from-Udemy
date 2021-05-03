#learning if elif else statement 
#boolean also


I_eat =True
I_drink = False


if I_eat:
    print("I wanna eat maggie")
elif I_drink:
    print("I wanna drink water")
else:
    print("no thanks")


if I_eat & I_drink:
    print("I will take all of your stock")
elif I_eat | I_drink:
    print("Its ok")
else:
   print("No Thanks Again")


if not I_eat:
    print("good work")
else  :
    print("not good")