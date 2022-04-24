# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Take both peoples names and
both_names = name1 + name2
lower_case_names = both_names.lower()

# then iterate through the names and find letter oc

love_score1 = 0
love_score2 = 0
for letters in lower_case_names:
    if letters == "t":
        love_score1 += 1
    if letters == "r":
        love_score1 += 1
    if letters == "u":
        love_score1 += 1
    if letters == "e":
        love_score1 += 1

    # 2nd iteration
    if letters == "l":
        love_score2 += 1
    if letters == "o":
        love_score2 += 1
    if letters == "v":
        love_score2 += 1
    if letters == "e":
        love_score2 += 1

love_score = int(str(love_score1) + str(love_score2))
if 10 <= love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
