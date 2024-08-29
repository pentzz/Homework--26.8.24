import random


def check_guess(lucky_number: int, user_guess: str) -> str:
    '''

    :param lucky_number: the random choice between 1-00
    :param user_guess:
    if the string is an int number and between 1-100 -if not raise ValueError
    if the string is not in range 1-100 ValueError "number out of range"

    :return:
    user_guess = lucky_number - return "BINGO!!"
    user_guess < lucky_number - return "guess higher"
    user_guess > lucky_number - return "guess lower"
    '''
    try:
        user_guess = int(user_guess)
    except ValueError:
        return "Invalid input"
    if not (1 <= user_guess <= 100):
        return "number out of range"
    if lucky_number == user_guess:
        return "Bingo"
    elif lucky_number > user_guess:
        return "guess higher"
    else:
        return "guess lower"

def play_guessing_game():
    lucky_number: int = random.randint(1, 100)
    user_guesses: int = 0
    try:
        while True:
            user_guess = input("Please guess a number between 1-100: ")
            feedback: str = check_guess(lucky_number, user_guess)
            print(feedback)
            user_guesses += 1
            if feedback == "Bingo":
                print(f"Great! you guessed the correct number:  {user_guess} in {user_guesses} guesses!")
                break
    except Exception as ex:
        print(ex)