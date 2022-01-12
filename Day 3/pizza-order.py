# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pizza_price = 0
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

# If the user orders a large pizza.
if size == "L":
    pizza_price += 25
    if add_pepperoni == "Y":
        pizza_price += 3
    if extra_cheese == "Y":
        pizza_price += 1
    print(f"Your final bill is: ${pizza_price}.")

# If user orders a Medium pizza.
if size == "M":
    pizza_price += 20
    if add_pepperoni == "Y":
        pizza_price += 3
    if extra_cheese == "Y":
        pizza_price += 1
    print(f"Your final bill is: ${pizza_price}.")

# If user orders a small pizza.
if size == "S":
    pizza_price += 15
    if add_pepperoni == "Y":
        pizza_price += 2
    if extra_cheese == "Y":
        pizza_price += 1
    print(f"Your final bill is: ${pizza_price}.")







