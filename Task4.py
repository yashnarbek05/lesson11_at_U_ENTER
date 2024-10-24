import os
import random

'''
 A Bingo card consists of 5 columns of 5 numbers. 
 The columns are labeled with the letters B, I, N, G 
 and O. There are 15 numbers that can appear under each 
 letter. In particular, the numbers that can appear under 
 the B range from 1 to 15, the numbers that can appear 
 under the I range from 16 to 30, the numbers that 
 can appear under the N range from 31 to 45, and so on.
 Write a function that creates a random Bingo card and 
 stores it in a dictionary. The keys will be the letters 
 B, I, N, G and O. The values will be the lists of five 
 numbers that appear under each letter. Write a second 
 function that displays the Bingo card with the columns 
 labeled appropriately. Use these functions to write a program 
 that displays a random Bingo card. Ensure that the main program 
 only runs when the file containing your solution has not been 
 imported into another program.
'''


def card_generator():
    B = random.randint(1, 16)
    I = random.randint(16, 31)
    N = random.randint(31, 46)
    G = random.randint(46, 61)
    O = random.randint(61, 76)

    return {
        "B": B,
        "I": I,
        "N": N,
        "G": G,
        "O": O
    }


def bingo_checker(b, i, n, g, o):
    cards = card_generator()
    return (b == cards.get("B")
            and i == cards.get("I")
            and n == cards.get("N")
            and g == cards.get("G")
            and o == cards.get("O")) ,cards


if __name__ == '__main__':
    b = int(input("Enter number [1,15] for B: "))
    i = int(input("Enter number [16,30] for I: "))
    n = int(input("Enter number [31,45] for N: "))
    g = int(input("Enter number [46,60] for G: "))
    o = int(input("Enter number [61,75] for O: "))

    i, cards = bingo_checker(b,i,n,g,o)

    if i: print("BINGO")
    else :
        print("true answers:", cards)
        print("better lunch next time :)")