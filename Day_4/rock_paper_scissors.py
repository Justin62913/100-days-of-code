import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Gather users choice and generate computers random choice
users_choice = int(input("What do you choose? 0 = Rock, 1 = Paper, 2 = Scissors. "))
rock_paper_scissors = [rock, paper, scissors]
computer_choice = random.choice(rock_paper_scissors)

# logic for calculating users choice and printing them out.
if users_choice == 0:
    if computer_choice == rock_paper_scissors[2]:
        print(rock)
        print(scissors)
        print(f"you picked Rock and computer picked Scissors, you win!!\n")
    else:
        print(rock)
        print(paper)
        print("paper covers rock, you lose!")

elif users_choice == 1:
    if computer_choice == rock_paper_scissors[0]:
        print(paper)
        print(rock)
        print(f"you picked paper and computer picked rock, you win!\n")
    else:
        print(paper)
        print(scissors)
        print("scissors cuts paper, you lose.")

elif users_choice == 2:
    if computer_choice == rock_paper_scissors[1]:
        print(scissors)
        print(paper)
        print(f"You picked scissors and computer picked paper, you win!\n")
    else:
        print(scissors)
        print(rock)
        print("rock smashes scissors, you lose.")



# seeing who won or lost.
# if users_choice == computer_choice:
#     print("Tie")
# elif users_choice == rock_paper_scissors[0]:
#     if computer_choice == rock_paper_scissors[1]:
#         print(f"you picked {users_choice} and computer picked {computer_choice}, you win!!\n" + rock)
#         print()
#     else:
#         print("paper covers rock, you lose.")
# elif users_choice == rock_paper_scissors[1]:
#     if computer_choice == rock_paper_scissors[0]:
#         print(f"you pciked {users_choice} and computer picked {computer_choice}, you win!\n" + paper)
#     else:
#         print("scissors cuts paper, you lose.")
# elif users_choice == rock_paper_scissors[2]:
#     if computer_choice == rock_paper_scissors[1]:
#         print(f"You picked {users_choice} and computer picked {computer_choice}, you win!\n" + scissors)
#     else:
#         print("rock smashes scissors, you lose.")






