import random

four_letter_word_bank = ["bake", "tide", "list",
             "bath", "cold", "hope", "hide", "cart",
             "game", "hate", "thin", "like", "bite",
             "dumb", "what", "rule", "play", "kite", "time"]
five_letter_word_bank = ["stand", "alone", "anger", "adopt", "brain", "below", "crazy","dozen", "enjoy","lucky","index","pitch","beach","watch","think"]
guess_record = []
wrong_letter = []
right_letter = []
games = 0
game_over = False

def guess_function(word):
    guesses = 1
    right_letter = []
    wrong_letter =[]
    while word != secret_word:
        for letter in word:
            if letter not in secret_word:
                if letter not in wrong_letter:
                    wrong_letter.append(letter)
            if letter in secret_word:
                if letter not in right_letter:
                    right_letter.append(letter)

        print("Nice try! Try again!")
        print("Right letters: " + str(sorted(right_letter)))
        print("Wrong letters: " + str(sorted(wrong_letter)))
        print()
        word = input("Type your guess: ")
        guesses+=1
    print()
    print("Correct! The secret word was: " + secret_word + "! Good job.\nIt took you " + str(guesses) + " tries.")
    guess_record.append(guesses)

print("Hello, welcome to Secret Word!")
print("Here's how to play!")
print()
print("You will be guessing a 4 or 5 letter word.")
print("We will show you the right and wrong letters after each guess.")
print()
print("Are you ready to play?")
ans = input("Type 'Yes' or 'yes' to start. ")

if ans == "yes" or "Yes":
    while not game_over:
        print()
        if games > 0:
            choice = input("Play another game?\n1. One more!\n2. View game statistics.\n3. I'm done playing.\n\nChoice: ")
            if choice == "3":
                print()
                print("Thanks for playing! See you next time.")
                break
            elif choice == "1":
                print()
                letter_choice = input("Do you want to guess a 4 or 5 letter word?\nEnter 4 or 5: ")
                secret_word = random.choice(four_letter_word_bank if letter_choice == "4" else five_letter_word_bank)
                print()
                if letter_choice == "4":
                    print("Great! We have chosen a 4-letter word.")
                    guess = input("Type your guess: ")
                    print(" ")
                    guess_function(guess)
                    games += 1
                elif letter_choice == "5":
                    print("Great! We have chosen a 5-letter word.")
                    guess = input("Type your guess: ")
                    print(" ")
                    guess_function(guess)
                    games += 1
            elif choice == "2":
                print()
                if games > 1:
                    print(f"You have played {games} games.\nIt took you at most {max(guess_record)} to guess the correct word.\nThe least amount of tries it took you was {min(guess_record)}.")
                else:
                    print(
                        f"You have played {games} game.\nIt took you {guess_record[0]} tries to guess the correct word.")


        else:
            print()
            letter_choice = input("Do you want to guess a 4 or 5 letter word?\nEnter 4 or 5: ")
            secret_word = random.choice(four_letter_word_bank if letter_choice == "4" else five_letter_word_bank)
            print()
            if letter_choice == "4":
                print("Great! We have chosen a 4-letter word.")
                guess = input("Type your guess: ")
                print(" ")
                guess_function(guess)
                games += 1
            elif letter_choice == "5":
                print("Great! We have chosen a 5-letter word.")
                guess = input("Type your guess: ")
                print(" ")
                guess_function(guess)
                games += 1