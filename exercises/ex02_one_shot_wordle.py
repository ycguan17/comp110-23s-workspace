"""EX02 - Attempts at a One-Shot Wordle."""

__author__ = "730372605"

secret: str = "python"
guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: str = ""
check: int = 0
char_found: bool = False
char_index: int = 0
while (len(guess) != len(secret)):
    guess = input("That was not " + str(len(secret)) + " letters! Try again: ")
while check < len(secret):
    if secret[check] == guess[check]:
        index = index + GREEN_BOX
    else:
        char_index = 0
        char_found = False
        while not char_found and char_index < len(secret):
            if secret[char_index] == guess[check]:
                char_found = True
            char_index = char_index + 1
        if bool(char_found) is True:
            index = index + YELLOW_BOX
        else:
            index = index + WHITE_BOX
    check = check + 1
print(index)
if (guess == secret):
    print("Woo. You got it! ")
else:
    print("Not quite. Play again soon!")
