import random
import sys

# Word lists (dictionaries kept for backward familiarity)
CARS = {
    1: 'bentley', 2: 'jaguar', 3: 'volkswagen', 4: 'ford', 5: 'tesla',
    6: 'porsche', 7: 'mclaren', 8: 'mercedes', 9: 'audi', 10: 'chevrolet',
    11: 'kia', 12: 'renault', 13: 'honda', 14: 'hyundai', 15: 'suzuki',
    16: 'subaru', 17: 'lexus', 18: 'mazda', 19: 'fiat', 20: 'jeep',
    21: 'acura', 22: 'ducati', 23: 'lamborghini'
}
ANIMALS = {
    1: 'horse', 2: 'fox', 3: 'lion', 4: 'tiger', 5: 'elephant',
    6: 'dog', 7: 'cat', 8: 'kangaroo', 9: 'zebra', 10: 'leopard'
}
PLACES = {
    1: 'gujarat', 2: 'new delhi', 3: 'agra', 4: 'varanasi', 5: 'shimla',
    6: 'alaska', 7: 'nairobi', 8: 'kenya', 9: 'jaisalmer', 10: 'brazil',
    11: 'australia'
}

VOWELS = set('aeiou')

def choose_word_from_category(cat_dict):
    """Prompt user to pick an index or 0 for random; return the chosen word (lowercase)."""
    min_idx = min(cat_dict.keys())
    max_idx = max(cat_dict.keys())
    while True:
        try:
            user = input(f"Select a number from {min_idx} to {max_idx} (or 0 for random): ").strip()
            if user == '':
                print("Please enter a number.")
                continue
            n = int(user)
            if n == 0:
                n = random.choice(list(cat_dict.keys()))
                print(f"Randomly selected number: {n}")
            if n < min_idx or n > max_idx:
                print(f"Please choose a number between {min_idx} and {max_idx} (or 0 for random).")
                continue
            return cat_dict[n].lower()
        except ValueError:
            print("Invalid input. Enter an integer.")
        except KeyError:
            print("Number out of range, try again.")

def make_display_word(word):
    """Return a list that exposes vowels and spaces, hides consonants as '_'."""
    return [ch if (ch in VOWELS or ch == ' ') else '_' for ch in word]

def print_display(display):
    """Nicely print display list with spaces between characters."""
    # Join with space so underscores and letters are visible clearly
    print(' '.join(display))

def play_round(word):
    """Play one round for the provided word. Returns True if user wins, False if loses."""
    word = word.lower()
    display = make_display_word(word)
    chances = 5
    guessed_letters = set()

    print("\nWord:")
    print_display(display)
    print("Chances left:", chances)

    while True:
        guess = input("\nEnter a single letter (or guess the whole word): ").strip().lower()
        if not guess:
            print("Please enter something.")
            continue

        # Full-word guess
        if len(guess) > 1:
            if guess == word:
                print("\nYou Win, Congratulations!!")
                return True
            else:
                chances -= 1
                print(f"Wrong guess for full word. Chances left: {chances}")
        else:
            # Single-letter guess
            g = guess
            if not g.isalpha():
                print("Please enter an alphabetic character.")
                continue

            if g in guessed_letters:
                print(f"You already guessed '{g}'. Try a different letter.")
                continue

            guessed_letters.add(g)

            if g in word:
                # Reveal all occurrences
                for i, ch in enumerate(word):
                    if ch == g:
                        display[i] = g
                print_display(display)
                print("Chances left:", chances)
            else:
                chances -= 1
                print_display(display)
                print(f"Wrong letter guessed. Chances left: {chances}")

        # Win condition
        if '_' not in display:
            print("\nYou Win, Congratulations!!")
            return True

        # Lose condition
        if chances <= 0:
            print("\nYou Lose, better luck next time.")
            print("The correct answer is:", word)
            return False

def main():
    print("Hello there, What is your name?")
    name = input().strip()
    if not name:
        name = "Player"
    print(f"Let us play a game, {name}\n")

    input("Read the instructions before playing (press Enter) ")
    input("This game is about guessing words (press Enter) ")
    input("Vowels of the word are shown, consonants are hidden. The word may contain spaces. Letters are lowercase. (press Enter) ")
    input("You will get 5 chances. Correct letters are revealed; wrong guesses cost 1 chance. (press Enter) ")

    print("\nEnter Y for yes and N for no")
    want_play = input("Want to play the game? (Y/N): ").strip().lower()
    while want_play == 'y':
        print("\nSelect a category:")
        print("1 - Cars")
        print("2 - Animals")
        print("3 - Places")
        cat = input("Enter category number (1/2/3): ").strip()
        if cat not in ('1', '2', '3'):
            print("Invalid category. Please enter 1, 2, or 3.")
            continue

        if cat == '1':
            print("You chose: Cars")
            word = choose_word_from_category(CARS)
        elif cat == '2':
            print("You chose: Animals")
            word = choose_word_from_category(ANIMALS)
        else:
            print("You chose: Places (may include spaces)")
            word = choose_word_from_category(PLACES)

        # Play one round with the selected word
        play_round(word)

        # Play again?
        print()
        want_play = input("Want to play the game again? (Y/N): ").strip().lower()
        while want_play not in ('y', 'n'):
            want_play = input("Please enter 'Y' or 'N': ").strip().lower()

    print("Okay, thank you for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
        sys.exit(0)
