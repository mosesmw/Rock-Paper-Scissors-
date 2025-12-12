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

computer_answer = random.randint(0, 2)

answer = int(input("What do you choose? '0' for rock '1' for paper and '2' for scissors: "))
if answer == 0:
    print(rock)
elif answer == 1:
    print(paper)
else:
    print(scissors)


if computer_answer == 0:
    print(rock)
elif computer_answer == 1:
    print(paper)
else:
    print(scissors)

if answer == computer_answer:
    print("It's a tie!")
elif answer == 0 and computer_answer == 2:
    print("You win!")
elif answer == 1 and computer_answer == 0:
     print("You win!")
elif answer == 2 and computer_answer == 1:
     print("You win!")
else:
    print("You lose!")






