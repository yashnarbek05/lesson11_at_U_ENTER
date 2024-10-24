import os

'''
Write a function that takes a string of characters as its first 
parameter, and the width of the terminal in characters as its 
second parameter. Your function should return a new string that
consists of the original string and the correct number of 
leading spaces so that the original string will appear centered
within the provided width when it is printed. Do not add any
characters to the end of the string. Include a main program
that demonstrates your function. 
'''

def print_on_center(str):
    i = os.get_terminal_size().columns
    print(" " * (int(i/2) - len(str)-1), str)

if __name__ == '__main__':
    print_on_center("men")

