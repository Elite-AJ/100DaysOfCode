import art

print(art.logo)

import random

# Start the program
start_game = input("Do you want to play a game of Blackjack? (y/n)  ")
if start_game == 'y':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    my_cards = random.choices(cards, k=2)
    comp_cards = random.choices(cards, k=2)

    def calculate_cards(x):
        total_cards = sum(x)
        # Handle the ace
        if 11 in x and total_cards > 21:
            x.remove(11)
            x.append(1)
        return total_cards
    
    my_total = calculate_cards(my_cards)
    comp_total = calculate_cards(comp_cards)

    # Print initial results
    print(f"Your cards: {my_cards}, current score: {my_total}")
    print(f"Computer's first card: {comp_cards[0]}")

    # Check for BlackJack
    if my_total == 21:
        print("BLACKJACK, You win!!!")
    elif comp_total == 21:
        print("BLACKJACK, Computer wins!!!")
    else:
        # Player's Turn
        game_active = True
        while game_active:
            next_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if next_card == 'y':
                new_card = random.choice(cards)
                my_cards.append(new_card)
                my_total = calculate_cards(my_cards)
                print(f"Your cards: {my_cards}, current score: {my_total}")
                if my_total > 21:
                    print("You went over 21. Computer wins!")
                    game_active = False
            else:
                # Computer's Turn
                while comp_total < 17:
                    new_card = random.choice(cards)
                    comp_cards.append(new_card)
                    comp_total = calculate_cards(comp_cards)
                
                print(f"Computer's final hand: {comp_cards}, final score: {comp_total}")

                # Determine the winner
                if comp_total > 21:
                    print("Computer went over 21. You win!")
                elif my_total > comp_total:
                    print("You win!")
                elif my_total < comp_total:
                    print("Computer wins!")
                else:
                    print("It's a tie!")
                
                game_active = False
else:
    print("Game ended.") 