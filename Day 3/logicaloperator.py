# if age is bertween 45 to 55 tikcet is free

print("Welcome to the Game and Photo Frama")
height = int(input("Enter Your Height: "))
age = int(input("Enter Your Age: "))

if height >= 120:
    print("You Can Ride Rollercoaster")
    if age >= 45 and age<= 55: #logical operator
        bill = 0
        print("You have free ride from our side")
    elif age >=12:
        bill = 7
        print("You Need to Pay: $7")
    else:
        bill = 5
        print("You Need to Pay: %5")

    wantobjects = input("Do you want to have Photo take? type y for yes and n for No.")
    if wantobjects == "y":
        bill += 3
    print(f"Your Final Bill is {bill}")
else:
    print("You Heigh is small, You Can't ride Rollercoaster")

