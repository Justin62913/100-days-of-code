# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# 🚨 Don't change the code above 👆
#Write your code below this line 👇
cal_bmi = weight / (height ** 2)

if cal_bmi < 18.5:
    print(f"Your BMI is {round(cal_bmi)}, you are underweight.")

elif 18.5 < cal_bmi < 25:
    print(f"Your BMI is {round(cal_bmi)}, you have a normal weight.")

elif 25 < cal_bmi < 30:
    print(f"Your BMI is {round(cal_bmi)}, you are slightly overweight.")

elif 30 < cal_bmi < 35:
    print(f"Your BMI is {round(cal_bmi)}, you are obese.")

else:
    print(f"Your BMI is {round(cal_bmi)}, you are clinically obese.")


