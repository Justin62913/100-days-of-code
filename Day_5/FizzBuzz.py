for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        FizzBuzz = "FizzBuzz"
        print(FizzBuzz)
    elif number % 5 == 0:
        number_Buzz = "Buzz"
        print(number_Buzz)
    elif number % 3 == 0:
        number_Fizz = "Fizz"
        print(number_Fizz)
    else:
        print(number)



