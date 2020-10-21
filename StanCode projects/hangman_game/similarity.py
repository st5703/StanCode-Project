"""
File: similarity.py
Name: Che-Hsien, Chiu
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    find the most similar fragment in an input DNA.
    """
    long_sequence_DNA = input('Please give me a DNA sequence to search : ')
    short_sequence_DNA = input('What DNA sequence would you like to match? ')
    similar_DNA = find_similar(long_sequence_DNA, short_sequence_DNA)
    print('The best match is ' +str(similar_DNA))


def find_similar(long_DNA, short_DNA):
    """
    :param long_DNA: string
    :param short_DNA: string
    :return: string
    """
    # the number of comparision
    count = len(long_DNA) - len(short_DNA) + 1

    # initialize similarity and best match DNA
    similarity = 0

    # compare each DNA fragment in long DNA
    for i in range(count):
        n = 0    # each character in short DNA
        match_count = 0
        for j in range(i,i+len(short_DNA)):    # different fragment starts from ith position of long DNA
            if (short_DNA[n].upper() == long_DNA[j].upper()):    # same DNA in same sequence
                match_count += 1    # match count + 1
            n+=1

        # check if the highest similarity
        if match_count > similarity:
            best_match = ''
            similarity = match_count
            for k in long_DNA[i:i+len(short_DNA)]:
                best_match += k.upper()

    return best_match




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
#    long_sequence_DNA = 'aTcgaTCgatCGC'
#    short_sequence_DNA ='TcGc'
    main()
