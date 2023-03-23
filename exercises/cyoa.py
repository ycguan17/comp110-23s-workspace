"""EX06 - Choose Your Own Adventure."""

__author__ = "730372605"

player: str = ""
points: int = 100


def secret() -> None:
    """Adds points based on name length of player."""
    global points 
    idx: int = 0
    while idx <= len(player):
        points = points + 20
        idx = idx + 1


def greet(name: str) -> None:
    """Asks for name and gives summary and greetings for the game."""
    global player
    player = input(player)
    print(f"Welcome to the Escape Game, {name}. Currently you are trapped within a mansion. All the doors are locked except for the kitchen, the bedroom and the basement. In order to escape, you must find the corrrect code to open the main door. P.S. Keep in mind that you start off with 100 adventure points, which you lose with each wrong combination given. Each wrong combo subtracts 20 points. P.P.S. Try inputting the game name for a surprise!~")


def main() -> None:
    """Main body of the game."""
    greet(player)
    num: int = 500
    points = 100
    ready: str = input(f"Are you ready to play {player} ? ")
    answer: str = num * 3
    if ready == "Yes" or "yes":
        choice: str = input("You have 3 options for starting points. Would you like to enter the kitchen, the bedroom or the basement first? ")
        kitchen_answer: int = num * 2 - num / 10
        basement_answer: int = num / 10 - 50
        bedroom_answer: int = num + 50
        kitchen: str = "You walk in with the door still creaking behind you. The first thing that enters your sight is the red ink dripping from the countertop. You walk over to find the following written on top: S " + str(num) + "x2 - " + str(num) + "/10"
        basement: str = "You walk in with the door still creaking behind you. The first thing that enters your sight is the catalog of the food in front of you. You notice a expression written on the : M " + str(num) + "/10 - 50"
        bedroom: str = "You walk in with the door still creaking behind you. The first thing that enters your sight is a embroidered pillow on teh bed. You walk over to find the following written on top: U " + str(num) + " + 50"
        if choice == "kitchen":
            print(kitchen)
            ip: int = input("What is the answer? Hint: The letter is important later!~ ")
            while ip != kitchen_answer:
                print("Oops, not quite! Try again.")
                points = points - 10
                print(ip)
            else:
                print("Congrats, on to the next room!")
                r: str = input("Are you ready to guess?")
                if r == "yes":
                    guess: int = input("Great! You head to the mansion door. On the side is a numberpad. What do you input?")
                    if guess != answer:
                        print("Oops, try again!")
                        points = points - 20
                else:
                    print(choice)
        if choice == "basement":
            print(basement)
            print(ip)
            while ip != basement_answer:
                print("Oops, not quite! Try again.")
                points = points - 20
                print(ip)
            else:
                print(r)
                if r == "yes":
                    print(guess)
                    if guess != answer:
                        print("Oops, try again!")
                        points = points - 20
                else:
                    print(choice)
        if choice == "bedroom":
            print(bedroom)
            print(ip)
            while ip != bedroom_answer:
                print("Oops, not quite! Try again.")
                points = points - 20
                print(ip)
            else:
                print(r)
                if r == "yes":
                    print(guess)
                    if guess != answer:
                        print("Oops, try again!")
                        points = points - 20
                else:
                    print(choice)
        else:
            print("Invalid response, please try again.")
    else:
        if ready == "Escape Game" or "escape game":
            print("You have found the secret point multiplier! As a reward for finding this function we will now add 20 times the lenghth of your name in points!")
            print(f"You now have {secret()} points!")
        if ready == "No" or "no":
            print("Thank you for choosing to play Escape Game!")
            return None
    print(f"Your final adventure points is {points} points.")
    if points <= 60:
        print("Better luck next time!")
    else:
        print("Good work!")
        if points > 100:
            print("Exceptional work! Glad you found the point multiplier~")


if __name__ == "__main__":
    main()