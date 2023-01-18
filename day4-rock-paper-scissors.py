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

#Write your code below this line 👇
choice = input("Pick an option \n 0 for Rock, 1 for Paper and 2 for Scissors: ")
player_choice = [rock, paper, scissors]
comp_choice = random.choice(player_choice)

if choice == ("0"):
  choice = rock
  print(f"{choice}  {comp_choice}")
  if choice == comp_choice:
    print("This is a tie")
  elif comp_choice == scissors:
    print("Rock crushes Scissors, Player wins")
  else:
    print("Paper covers Rock, CPU wins")
elif choice == ("1"):
  choice = paper
  print(f"{choice} {comp_choice}")
  if choice == comp_choice:
    print("This is a tie")
  elif comp_choice == rock:
    print("Paper covers Rock, Player wins")
  else:
    print("Scissors cuts Paper, CPU wins")
elif choice == ("2"):
  choice = scissors
  print(f"{choice} {comp_choice}")
  if choice == comp_choice:
    print("This is a tie")
  elif comp_choice == paper:
    print("Scissors cuts Paper, Player wins")
  else:
    print("Rock crushes Scissors, CPU wins")
else:
  print("Invalid selection")
