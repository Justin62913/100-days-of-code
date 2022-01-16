# 🚨 Don't change the code below 👇
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_name_index = random.randrange(len(names))
random_lst_names = names[random_name_index]
print(f"{random_lst_names} is going to buy the meal today!")



