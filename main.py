import random
from game_data import data
from art import logo
from art import vs
score=0
print(logo)
a=random.choice(data)
b=random.choice(data)
game_over=True
while game_over:
    print(f"Compare A:{a['name']},{a['description']} from {a['country']}")
    print(vs)
    print(f"Compare B:{b['name']},{b['description']} from {b['country']}")

    a_or_b=input("Who has more followers? Type 'A' or 'B':").upper()
    if a_or_b=="A":
         if a['follower_count']>b['follower_count']:
             score+=1
             c=random.choice(data)
             a=b
             b=c
             print(logo)
             print(f"You're right! Current score: {score}.")


         elif a['follower_count']<b['follower_count']:
             game_over=False
             print(logo)
             print(f"Sorry, that's wrong. Final score: {score}")
    elif a_or_b=="B":
         if a['follower_count']<b['follower_count']:
             score+=1
             c=random.choice(data)
             a=b
             b=c
             print(logo)
             print(f"You're right! Current score: {score}.")

         elif a['follower_count']>b['follower_count']:
             game_over=False
             print(logo)
             print(f"Sorry, that's wrong. Final score: {score}")