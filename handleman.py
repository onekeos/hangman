from random import randint


def game():
    word_bank = ['python', 'java', 'kotlin', 'javascript']
    lives = 8
    correct_word = word_bank[randint(0, len(word_bank) - 1)]
    tip_list = ['-'] * len(correct_word)
    print("\nLet's play")
    print('Try guess a word\n')

    while lives != 0:
        tip = ''.join(tip_list)
        if '-' in tip_list:
            print(tip)
            guess_letter = input(f'Input a letter: ')
            if len(guess_letter) == 1:
                if guess_letter in set(correct_word):
                    for i in range(len(correct_word)):
                        if guess_letter == correct_word[i]:
                            tip_list[i] = correct_word[i]
                    else:
                        print()
                else:
                    lives -= 1
                    print('No such letter in the word')
                    print(f'Num of lives: {lives}')
                    print()
            else:
                print('Only one symbol!\n')
        else:
            print(f'The word: {correct_word}. You won!')
            print('Thanks for playing!\n')
            break
    else:
        print('You loose!')


def menu():
    print('\nH A N G M A N\n')
    choice = input('Wanna play? ').lower()
    if choice == 'yes':
        while choice == 'yes':
            game()
            choice = input('New game? ')
            print('Good bye!\n')
    elif choice == 'no':
        print('Good bye!\n')
    else:
        print('Only Yes or No')
        menu()


menu()
