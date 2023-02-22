"""Structured Wordle."""

__author__ = "730372605"


def contains_char (word: str, char: str) -> bool:
    """Declare whether we can find char within searched word/letters."""
    assert len(char) == 1
    check: int = 0
    while check < len(word):
        if word[check] == char:
            return True
        else:
            check = check + 1
    return False


def emojified (guess: str, secret: str) -> str:
    """codifies two strings of the same length based on how close the words are to one another."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: str = ""
    check: int = 0
    while check < len(secret):
        if secret[check] == guess[check]:
            index = index + GREEN_BOX
        else:
            if contains_char(secret, guess[check]) is True:
                index = index + YELLOW_BOX
            else:
                index = index + WHITE_BOX
        check = check + 1
    return index


def input_guess (max_input: int) -> str:
    """Put in a guess that fits the length given."""
    guess: str = input("Enter a " + str(max_input) + " character word: ")
    while len(guess) != max_input:
        guess = input("That wasn't " + str(max_input) + " chars! Try again: ")
    return guess


def main() -> None:
    """The entry point of program and the main game loop."""
    secret: str = "codes"
    current_round: int = 1
    while current_round <= 6:
        print(f"=== Turn {current_round}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified (guess, secret))
        if guess == secret:  
            print(f"You won in {current_round}/6 turns!")
            exit()
        current_round = current_round + 1
    if guess != secret and current_round > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()