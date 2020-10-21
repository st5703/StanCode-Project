"""
File: anagram.py
Name: Che-Hsien Chiu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []
# count = 0


def main():
    read_dictionary(FILE)
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    while True:
        word = input('Find anagrams for: ')
        # check EXIT or search
        if word == EXIT:
            break
        else:
            anagram_list = find_anagrams(word)
            print(f'{len(anagram_list)} anagrams : {anagram_list}')


def read_dictionary(file):
    """
    :param file: (string) file name
    """
    global dict_list
    with open(file, 'r') as f:
        for line in f:
            dict_list.append(line.split('\n')[0])    # remove '\n'


def find_anagrams(s):
    """
    :param s: (string) search word
    :return: (list) anagram list
    """
    char_dict = {}
    for i in s:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    print('Searching...')
    return find_anagrams_helper(s, char_dict, [], '')


def find_anagrams_helper(s, char_dict, anagram_lst, ch):
    """
    :param s: (string) search word
    :param char_dict: (dict) char dict made from s
    :param anagram_lst: (list) anagram list
    :param ch: (string) word during searching
    :return: (list) anagram list
    """
    # Base Case, length of anagram == length of searching word
    if len(ch) == len(s):
        if ch in dict_list:    # check if ch in dict_list
            print(f'Found: {ch}')
            anagram_lst.append(ch)
            print('Searching...')
        return anagram_lst

    # Recursive Case
    else:
        for i in s:    # choose from char_dict
            if i not in char_dict:
                pass
            elif char_dict[i] == 1:    # only one in char_dict
                char_dict.pop(i)
                if has_prefix(ch+i) and not in_anagram_list(anagram_lst, ch+i):    # check has prefix and repeat search
                    anagram_lst = find_anagrams_helper(s, char_dict, anagram_lst, ch+i)    # explore
                char_dict[i] = 1    # un choose
            else:    # more than one in char_dict
                char_dict[i] -= 1
                if has_prefix(ch+i) and not in_anagram_list(anagram_lst, ch+i):     # check has prefix and repeat search
                    anagram_lst = find_anagrams_helper(s, char_dict, anagram_lst, ch + i)    # explore
                char_dict[i] += 1    # un choose
        return anagram_lst


def has_prefix(sub_s):
    """
    :param sub_s: (string)
    :return: (boolean)
    """
    global dict_list
    for i in dict_list:
        if i.startswith(sub_s):
            return True
    return False


def in_anagram_list(anagram_list, sub_s):
    """
    check if sub_s has already exist in anagram list, avoid repeating search
    :param anagram_list: (list) anagram list
    :param sub_s: (string)
    :return: (boolean)
    """
    for i in anagram_list:
        if i.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
