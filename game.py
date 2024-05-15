secret_number = 25
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("lucky guess huhh")
        break
    elif guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print("too high")