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
import random

player=int(input('Type 0 for rock,1 for paper,2 for scissors '))



computer=[rock, paper, scissors]
player1=computer[player]

computer=random.choice(computer)
print(f'player\n{player1}\ncomputer\n{computer}')
if computer == rock :
  s=0
elif computer==paper:
  s=1
else:
  s=2

s=str(s)
player=str(player)

a=int(s+player)
print(a)

if a==1 or a==12 or a==20:
  print('You win')
elif s==11 or s==22 or s==33:
  print('Its a tie')
else:
  print("You lose")
