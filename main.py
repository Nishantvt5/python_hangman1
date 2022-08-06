import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 15

    while len(word_letter) > 0 and lives > 0:
        print("you have ", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print('')

            else:
                lives -= 1
                print("\n Your letter ,", user_letter, 'is not in the word')

        elif user_letter in used_letters:
            print("you have already used this letter, guess another letter.")

        else:
            print('That is not valid letter')

    if lives == 0:
        print('you died, sorry. the word was', word)
    else:
        print('yay! you guessed the word', word, '!!!!')


if __name__ == "__main__":
    hangman()



