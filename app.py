secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    guess_count += 1
    if guess == secret_number:
        print('You win the game, Congrats!')
        break

else:
    print('Sorry, Game Over')