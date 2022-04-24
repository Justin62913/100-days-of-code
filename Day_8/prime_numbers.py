# Write your code below this line 👇
def prime_checker(number):
    if number > 1:
        for i in range(2, number//2):
            if (number % i) == 0:
                print(f"It's not a prime number.")
                break
        else:
            print(f"It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


