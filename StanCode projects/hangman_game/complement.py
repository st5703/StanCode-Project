"""
File: complement.py
Name: Che-Hsien, Chiu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    analyze the complement of an input DNA
    """
    DNA = input('Please give me a DNA strand and I\'ll find the complement: ')
    print ('The complement of ' + DNA + ' is ' + str(complement(DNA)))


def complement(DNA):
    """
    :param DNA: string
    :return: string
    """
    complement_DNA =''
    for i in DNA:
        if i.upper() == 'A':
            complement_DNA += 'T'
        elif i.upper() == 'T':
            complement_DNA += 'A'
        elif i.upper() == 'G':
            complement_DNA += 'C'
        else:
            complement_DNA += 'G'

    return complement_DNA


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
#    DNA = 'atc'
    main()
