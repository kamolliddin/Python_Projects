from random import randint

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
options = [rock, paper, scissors]

user_choose = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
while(1):
    if user_choose in range(0, 3):
        print(options[user_choose])
        break
    else:
        user_choose = int(input("please type 0, 1 or 2: "))

computer_choose = randint(0, 2)
print(f"Computer chose: \n {options[computer_choose]}")

if user_choose == computer_choose:
    print("It's a tie!")
elif user_choose == 0:
    if computer_choose == 1:
        print("You lose !")
    elif computer_choose == 2:
        print("You win !")
elif user_choose == 1:
    if computer_choose == 0:
        print("You win !")
    elif computer_choose == 2:
        print("You lose !")
elif user_choose == 2:
    if computer_choose == 0:
        print("You lose !")
    elif computer_choose == 1:
        print("You win !")