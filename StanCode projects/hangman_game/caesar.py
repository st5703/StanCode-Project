"""
File: caesar.py
name : Che-Hsien, Chiu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    decipher a secret string
    """
    n = int(input ('Secret number: '))
    secret_string = input('What\'s the ciphered string: ')
    print('The deciphered string is :' +decipher(secret_string, n))


def decipher(secret_string, n):
    """
    translating old alphabet to new alphabet by shifting n position
    :param secret_string: string
    :param n: integer
    :return: string
    """
    # create empty string
    deciphered_string = ''

    # convert every character in secret string
    for i in secret_string:
        if i.isalpha():
            # find i's position in ALPHABET with case-insensitive way
            position = ALPHABET.find(i.upper())
            deciphered_string += ALPHABET[(position+n)%26]    # use the remainder to find the character
        else:
            deciphered_string += i
    return deciphered_string


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
#    n = 7
#    secret_string = 'rHn TKx MAx UXlM!'
    main()
