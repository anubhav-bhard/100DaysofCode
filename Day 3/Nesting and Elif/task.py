#scenerio: 1
#If age is >= 18 then pay 12 dollar rest 7 dollar and if height is > 120 then can ride else not
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("Enter Your Age: "))
if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 18:
        print("You need to Pay 7$")
    else:
        print("You need to pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")


#Scenerio: 2
# <12 "$5"
# 12-18 "$7"
# >18 "$12

print("Welcome to the rollercoaster! Scenerio2")
if height >= 120:
    print("You can ride the rollercaster")
    if age <= 12:
        print("Please Pay $5")
    elif age  < 18:
        print("Please Pay $7")
    else:
        print("Please Pay $12")
else:
    print("Sorry you can not ride rollercaster.")