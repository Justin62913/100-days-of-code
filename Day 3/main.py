# Roller Coaster Ticket/Ride
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
# Checks the age of the Person wanting to ride.
if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age > 18:
        bill = 12
    elif 18 >= age >= 12:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok, have a free ride on us!")
    else:
        bill = 5

# Asks that person if he/she wants a photo taken.
    wants_photo = input("Do you want a photo taken? type Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry you can't ride!")






