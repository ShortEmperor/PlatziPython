#!/usr/bin/env python

def main():

    number = int(input('Give me a number: \n>>'))

    if number%2 == 0 and number%4 == 0:
        print(f'The number {number} is a multiple of 4')
    elif number%2 == 0:
        print(f'The number {number} is even')
    else:
        print(f'The number {number} is odd')

if __name__=="__main__":
    main()
