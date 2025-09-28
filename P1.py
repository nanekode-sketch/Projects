import p1_random as p1
rng = p1.P1Random()

hand = 0
game = 0
player_wins = 0
dealer_wins = 0
ties = 0


game_over = False

while not game_over:
    game+=1
    print(f"START GAME #{game}")

    print()

    card = rng.next_int(13) + 1
    if card == 1:
        hand += 1
        print()
        print(f"Your card is a ACE!\nYour hand is: {hand}")
    elif card == 11:
        hand += 10
        print()
        print(f"Your card is a JACK!\nYour hand is: {hand}")
    elif card == 12:
        hand += 10
        print()
        print(f"Your card is a QUEEN!\nYour hand is: {hand}")
    elif card == 13:
        hand += 10
        print()
        print(f"Your card is a KING!\nYour hand is: {hand}")
    else:
        hand += card
        print()
        print(f"Your card is a {card}!\nYour hand is: {hand}")

    while True:

        print()
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
        print()
        choice = input("Choose an option: ")

        if choice == "1":
            card = rng.next_int(13) + 1
            if card == 1:
                hand += 1
                print()
                print(f"Your card is a ACE!\nYour hand is: {hand}")
            elif card == 11:
                hand += 10
                print()
                print(f"Your card is a JACK!\nYour hand is: {hand}")
            elif card == 12:
                hand += 10
                print()
                print(f"Your card is a QUEEN!\nYour hand is: {hand}")
            elif card == 13:
                hand += 10
                print()
                print(f"Your card is a KING!\nYour hand is: {hand}")
            else:
                hand += card
                print()
                print(f"Your card is a {card}!\nYour hand is: {hand}")

            if hand == 21:
                print("BLACKJACK! You win!")
                print()
                hand = 0
                player_wins+=1

                break
            if hand > 21:
                print("You exceeded 21! You lose.")
                print()
                hand = 0
                dealer_wins+=1

                break

        elif choice == "2":
            dealer = rng.next_int(11) + 16
            print()
            print(f"Dealer's hand: {dealer}\nYour hand is: {hand}")
            print()
            if dealer > 21:
                print("You win!")
                print()
                player_wins+=1
                hand = 0

                break
            elif dealer == 21:
                print("Dealer wins!")
                print()
                dealer_wins+=1

                hand = 0
                break
            elif dealer > hand:
                print("Dealer wins!")
                print()
                dealer_wins+=1
                hand = 0

                break
            elif hand > dealer:
                print("You win!")
                print()
                player_wins+=1
                hand = 0

                break
            elif hand == dealer:
                print("It's a tie! No one wins!")
                print()
                ties+=1
                hand = 0

                break

        elif choice == "3":
            print()
            win_ratio = (player_wins / (game-1) )*100
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {ties}")
            print(f"Total # of games played is: {game-1}")
            print(f"Percentage of Player wins: {win_ratio:.1f}%")

        elif choice == "4":
            game_over = True
            break

        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")





