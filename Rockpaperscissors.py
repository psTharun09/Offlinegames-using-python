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
num_to_choose=int(input("What do you chose?Type 0 for rock,1 for paper or 2 for Scissors. "))
if num_to_choose == 0:
    print(rock)
elif num_to_choose == 1:
    print(paper)
elif num_to_choose == 2:
    print(scissors)
else:
    print("INVALID INPUT!")

print("Computer chose:")
comp=[rock,paper,scissors]
print(random.choice(comp))

if num_to_choose == 0 and random.choice(comp) == rock:
    print("it's a draw")
elif num_to_choose == 0 and random.choice(comp) == paper:
    print("You lose")
elif num_to_choose == 0 and random.choice(comp) == scissors:
    print("You Won")
elif num_to_choose == 1 and random.choice(comp) == rock:
    print("You Won")
elif num_to_choose == 1 and random.choice(comp) == paper:
    print("it's a draw")
elif num_to_choose == 1 and random.choice(comp) == scissors:
    print("You lose")
if num_to_choose == 2 and random.choice(comp) == rock:
    print("You lose")
elif num_to_choose == 2 and random.choice(comp) == paper:
    print("You Won")
elif num_to_choose == 2 and random.choice(comp) == scissors:
    print("it's a draw")
else:
    print(" ")



