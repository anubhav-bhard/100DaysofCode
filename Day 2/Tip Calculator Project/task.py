print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_per_percentage = tip / 100
tip_total_amount = bill * tip_as_per_percentage
total_bill = bill + tip_total_amount
print(total_bill)
each_person_pay = total_bill/people
each_person_pay1 = round(each_person_pay, 2)
print(f"Each person should pay: {each_person_pay1}")
#print("Each Person Should Pay: " + a)
from tkinter.font import names

print(6 + 4/2-(1*2))
b=int("5") / int(2.7)
print(b)
#6+2-2

name=input("What is your name?")
print(f"Hello, {name}")
print("Hello," + name)

age=12
print(f"you are {age} years old" )
print("You are " + age + "years old") # this will not work bcz f string is not there so integer is not converted into string