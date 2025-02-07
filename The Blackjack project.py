import random
import art
def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    continues = True
    while continues:
        condition = True
        y_n1=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if y_n1 == "y":
            print(art.logo)


            a=random.choice(cards)
            b=random.choice(cards)
            c=a+b
            computer_a=random.choice(cards)
            computer_b=random.choice(cards)
            computer_c=computer_a+computer_b
            computer_d=0
            print(f'      Your cards:[{a},{b}] , current score:{c}')
            print(f"      Computer's first card:{computer_a}")

            while computer_c<=16:
                computer_e=[]
                computer_d=random.choice(cards)
                computer_c+=computer_d
                computer_e.append(computer_d)
            if (a == 11 and b == 11) or (computer_a == 11 and computer_b == 11):
                if a == 11 and b == 11:
                    a=1
                else:
                    computer_a=1


            if computer_a == 10 and computer_b == 10:
                print(f'      Your final hand:[{a},{b}] , final score:{c}')
                print(f"      Computer's final hand:[{computer_a},{computer_b}],  final score:{computer_c}")
                print("It's Blackjack!!!")
                print("You went over. You lose 😭")
                condition=False

            elif (a == 10 and b == 10) and not (computer_a == 10 and computer_b == 10):
                print(f'      Your final hand:[{a},{b}] , final score:{c}')
                print(f"      Computer's first hand:[{computer_a}],  final score:{computer_c}")
                print("It's Blackjack!!!")
                print("Opponent went over. You win 😁")
                condition=False
            elif (a==10 and b==11) or (a==11 and b==10):
                print(f'      Your final hand:[{a},{b}] , final score:{c}')
                print(f"      Computer's first hand:[{computer_a}],  final score:{computer_a}")
                print("Opponent went over. You win 😁")
                condition=False

            while   condition:
                game_over = True
                while game_over:
                    y_n2 = input("Type 'y' to get another card, type 'n' to pass:").lower()

                    if y_n2 == "y":
                        d = random.choice(cards)
                        c2 = c + d
                        print(f"     Your cards: [{a},{b},{d}], current score: {c2}")
                        print(f"      Computer's first card: {computer_a}")


                        y_n3 = input("Type 'y' to get another card, type 'n' to pass:").lower()
                        if y_n3 == "y":
                            e = random.choice(cards)
                            c3 = c2 + e
                            print(f"     Your cards: [{a},{b},{d},{e}], current score: {c3}")
                            print(f"      Computer's first card: {computer_a}")
                        elif y_n3 == "n":
                            game_over=False
                            condition=False
                            print(f"     Your final hand: [{a},{b},{d}], current score: {c2}")
                            print(f"      Computer's final hand:[{computer_a}],[{computer_b}],{computer_e} {computer_c}")
                            if computer_c>21:
                                print("Opponent went over. You win 😁")
                            elif  c2>21:
                                print("You went over. You lose 😭")
                            elif computer_c > c2:
                                print("You went over. You lose 😭")
                            elif c2 > computer_c:
                                print("Opponent went over. You win 😁")
                            elif c2 == computer_c:
                                print("It's an draw!!!!!")

                    if y_n2 == "n":
                        game_over = False
                        condition=False
                        print(f'      Your final hand:[{a},{b}] , current score:{c}')
                        print(f"      Computer's final hand:[{computer_a}],[{computer_b}],{computer_e} {computer_c}")
                        if computer_c > 21:
                            print("Opponent went over. You win 😁")
                        elif c > 21:
                            print("You went over. You lose 😭")
                        elif computer_c > c:
                            print("You went over. You lose 😭")
                        elif c > computer_c:
                            print("Opponent went over. You win 😁")
                        elif c == computer_c:
                            print("It's an draw!!!!!")


        if y_n1=="n":
            continues=False


black_jack()