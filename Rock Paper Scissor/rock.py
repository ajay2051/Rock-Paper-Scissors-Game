from random import randint

user_input = ['rock', 'paper', 'scissors']

while True:
    computer = user_input[randint(0, 2)]
    command = input("Enter command")
    if command == 'end game':
        print('Game Ended')
        break

    elif command == computer:
        print('Tie')
    
    elif command == 'rock':
        if computer == 'paper':
            print('You lose')
        else:
            print('You won')
    
    elif command == 'paper':
        if computer == 'scissors':
            print('You lose')
        else:
            print('You Won')
    
    elif command == 'scissors':
        if computer == 'paper':
            print('You lose')
        else:
            print('You won')
    else:
        print('Wrong Command...')

