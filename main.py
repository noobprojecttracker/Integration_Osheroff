# Mark Schwartz
# This is a simple Tic Tac Toe game. I draw the board with a dictionary. I keep track of which letter's turn
# it is by using a variable named turns. I have two functions which run every iteration of the loop, and terminate
# the game when a winner/draw is found. I then offer the user the ability to replay the game.
import time


print('Welcome to Tic Tac Toe, grab a friend and get ready to duel in this Python interpretation of the classic'
      ' game!\n')

time.sleep(3)  # I added this to give the user a brief time to read the welcome statement.


def print_board(spots):   # this function prints the board
    board = f'{spots[1]} | {spots[2]} | {spots[3]}\n{spots[4]} | {spots[5]} | {spots[6]}\n{spots[7]} | {spots[8]} | ' \
            f'{spots[9]}\n'
    print(board)


def integration():
    print('I will now explain the use of some python operators which I could not include in my game.')
    time.sleep(3)
    print('The ** operator in python is used to raise an integer or float to another integer or float.')
    print('Here is an example of that operator in use: ')
    print('3 ** 2 is equal to', 3 ** 2, '\n')
    time.sleep(5)
    print('The * operator in python completes simple multiplication. For example, 5 * 3 will print', 5 * 3, '\n')
    time.sleep(5)
    print('The operator / is used to do division in python between 2 integers or floats.')
    print('For example, the statement 5 / 2 will print', 5 / 2, '\n')
    time.sleep(5)
    print('The // operator in python is used to do floor division. It divides 2 numbers and then rounds the result'
          ' down to the nearest integer.')
    print('For example, the statement 10 // 3 in python will print', 10 // 3, '\n')
    time.sleep(5)
    print('The + operator in python is used to complete addition. For example, the statement 5 + 1 will print',
          5 + 1, '\n')
    time.sleep(5)
    print('The - operator in python is used to complete subtraction. For example, the statement 3 - 2 will print',
          3 - 2)
    time.sleep(5)
    print('The sep= operator in python is used to add a separator between items that need to be printed. '
          'For example, the statement print(1,3,5,sep="-") will print 1-3-5')
    print(1, 3, 5, sep='-')


def find_winner(spots):  # can detect any winner on horizontal, vertical, or diagonal spaces
    # check rows
    for i in range(3):
        row_start = 3*i + 1
        if spots[row_start] == spots[row_start + 1] == spots[row_start + 2]:
            return True
        col_start = i + 1
        if spots[col_start] == spots[col_start + 3] == spots[col_start + 6]:
            return True
    if spots[1] == spots[5] == spots[9]:
        return True
    if spots[3] == spots[5] == spots[7]:
        return True

    return False

    # if spots[1] == spots[2] == spots[3]:
    #     return True
    # elif spots[4] == spots[5] == spots[6]:
    #     return True
    # elif spots[7] == spots[8] == spots[9]:
    #     return True
    # elif spots[1] == spots[4] == spots[7]:
    #     return True
    # elif spots[3] == spots[6] == spots[9]:
    #     return True
    # elif spots[1] == spots[5] == spots[9]:
    #     return True
    # elif spots[3] == spots[5] == spots[7]:
    #     return True
    # elif spots[2] == spots[5] == spots[8]:
    #     return True
    # else:
    #     return False


def find_draw(available_spots):    # I detect a draw if all spots are full and no winner is found
    if not available_spots:
        return True


def wants_to_play_again():
    play_again = input('Do you wanna play again?\nPress (a) to continue... \nPress any other key to learn about'
                       ' some operators in Python!:')
    if play_again == 'a':
        print('Ok', end='\n')
        return True
    else:
        print('\nWelcome to your introduction to Python!')
        return False


def create_user():
    user = input('Enter a letter to represent your user: ')
    while len(user) > 1: # The > operator checks to see if the left value is greater than the right value
        user = input('Enter a letter to represent your user: ')
    return user


def change_a_spot(a_user, spots, available_spots):
    continue_loop = True
    while continue_loop:
        try:
            where_to_change = int(input('Choose a spot to land on: '))
            if where_to_change in available_spots:
                continue_loop = False
            elif where_to_change not in available_spots:
                print('Sorry ' + a_user + ', this spot is unavailable! Try again...') # The + string operator
                # concatenates two strings together
        except ValueError:
            print('That is not a spot!')

    spots[where_to_change] = a_user
    available_spots.remove(where_to_change)
    return True


def congratulate_winner(a_user):
    print('Congratulations, '*3, a_user, 'has won') # The * string operator prints a string multiple times


def announce_draw():
    print('A draw has been detected!')


def main():
    spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
             9: '9'}  # I draw the board with this dictionary

    available_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # I track available spots in this list. once a spot is chosen,
    # I remove it from this list

    user_one = create_user()
    user_two = create_user()
    turns = 0
    letter = None

    while True:

        if turns % 2 == 0 and (turns % 2 != 1): # The % operator returns the remainder after dividing two values
            letter = user_one
        elif turns % 2 != 0 or (turns % 2 == 1):
            letter = user_two

        print_board(spots)

        if change_a_spot(letter, spots, available_spots):
            turns += 1

        if find_winner(spots):
            print_board(spots)
            congratulate_winner(letter)
            break

        elif find_draw(available_spots):
            print_board(spots)
            announce_draw()
            break

    integration()


if __name__ == '__main__':
    main()
