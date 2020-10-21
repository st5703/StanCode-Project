"""
File: hangman.py
Name: Che-Hsien, Chiu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    guess a vocabulary in a hangman program
    """
    # initialize life, answer
    word = random_word()
    ans = answer(word)
    life = N_TURNS

    # start guessing
    while(life != 0):
        hangman_graph(life)
        print('The word looks like: ' +ans)
        print('You have ' +str(life) + ' guesses left.')
        guess = input('Your guess: ')

        # check if illegal format
        while is_illegal_format(guess):
            print('Illegal foramt.')
            guess = input('Your guess: ')

        # check if guess is correct
        if word.find(guess.upper()) != -1:
            print('You are correct!')
            print('')
            ans = update_ans(guess, word, ans)

            # check if guess is completed.
            if complete(ans):
                break
        else:
            life-=1
            print('There is no ' + guess.upper() + '\'s in the word.')
            print('')


    # guess finish, check result
    if (life == 0):    # no life, lose
        lose()
        print('You are completely hung : (')
        print('The word was : ' +word)
    else:    # still have life, win
        win()
        print('You win!!')
        print('The word was : ' + word)


def is_illegal_format(guess):
    """
    :param guess: string or integer
    :return: boolean
    """
    if len(guess) > 1:
        return True
    elif guess.isalpha():
        return False
    else:
        return True



def answer(word):
    """
    initialize an answer space.
    :param word: string
    :return: string
    """
    ans = ''
    for i in range(len(word)):
        ans += '-'
    return ans


def update_ans(guess, word, ans):
    """
    update guess character to answer string
    :param guess: string
    :param word: string
    :param ans: string
    :return:
    """

    guess_in_word = ''

    # find guess in word
    for i in word:
        if guess.upper() == i:
            guess_in_word += i
        else:
            guess_in_word += '-'

    # merge new answer with old answer
    ans = merge(guess_in_word, ans)

    return ans


def merge(guess_in_word, ans):
    """
    merge new answer with old answer
    :param new_ans: string
    :param ans: string
    :return: string
    """
    # create merge string
    merge_ans = ''

    # compare each position in old/new answer
    for i in range(len(ans)):

        # if not exists in the old answer
        if ans[i] == '-':
            if guess_in_word[i] != '-':    # guess is correct in new answer
                merge_ans += guess_in_word[i]
            else:    # keep unknown
                merge_ans += ans[i]

        # already exists in old answer, keep character
        else:
            merge_ans += ans[i]

    return merge_ans


def complete(ans):
    """
    :param ans: string
    :return: boolean
    """
    for i in ans:
        if i == '-':
            return False
    return True


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hangman_graph(life):
    """
    draw hang man graph by life count
    :param life: integer
    """
    if life == 7:
        stage()
    elif life == 6:
        head()
    elif life == 5:
        body()
    elif life == 4:
        left_hand()
    elif life == 3:
        right_hand()
    elif life == 2:
        left_foot()
    else:
        right_foot()







def stage():
    """
    hang man stage
    """
    print('=========')
    print('|   |     ')
    for i in range(5):
        print('|')
    print('____________________')


def head():
    """
    hang man head part
    """
    print('=========')
    print('|   |     ')
    print('|   O')
    for i in range(4):
        print('|')
    print('____________________')


def body():
    """
    hang man body part
    """
    print('=========')
    print('|   |     ')
    print('|   O')
    print('|  ( )')
    for i in range(3):
        print('|')
    print('____________________')

def left_hand():
    """
    hang man left hand part
    """
    print('=========')
    print('|   |     ')
    print('|   O')
    print('| /( )')
    for i in range(3):
        print('|')
    print('____________________')


def right_hand():
    """
    hang man right hand part
    """
    print('=========')
    print('|   |     ')
    print('|   O')
    print('| /( )\\')
    for i in range(3):
        print('|')
    print('____________________')

def left_foot():
    """
    hang man left foot part
    """
    print('=========')
    print('|   |     ')
    print('|   O')
    print('| /( )\\')
    print('|  / ')
    for i in range(2):
        print('|')
    print('____________________')

def right_foot():
    """
    hang man right foot part
    """
    print('=========')
    print('|   |     ')
    print('|   O <(help!!!!!)')
    print('| /( )\\')
    print('|  / \\')
    print('|    one life left!!!!!')
    print('|')
    print('____________________')

def lose():
    """
    dead graph
    """
    print('=========')
    print('|   |     ')
    print('|   x')
    print('| /( )\\')
    print('|  / \\')
    print('|        You Dead!!!')
    print('|')
    print('____________________')


def win():
    """
    win graph, Jerry show up
    """
    print('=========')
    print('|   |     ')
    print('|')
    print('|')
    print('|          Jerry : Congratulation!!! You win $100000 scholarship')
    print('|　　 O     O   ')
    print('|   -()-  \||/　')
    print('_____/\\____/\\_______')



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
