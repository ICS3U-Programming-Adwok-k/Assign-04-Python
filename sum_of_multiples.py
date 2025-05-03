#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: May 2nd, 2025
# This program displays all multiples of 3 or 5
# from 0 to 1000 and displays the sum of all numbers.


def main():
    print("Hello and welcome to my class")
    # The sum starts at 0
    sum = 0
    # for loop used to identify that range of
    # numbers from where it starts to where it ends
    for number in range(0, 1000):
        # if the number is divided by 3 or 5 and has no remainder
        if number % 3 == 0 or number % 5 == 0:
            # Display the number's
            print(number)
            # sum = sum + number
            sum = sum + number

    # displays the sum of the multiples of 3 or 5 below 1000.
    print(f"The sum of all multiples of 3 or 5 below 1000 is {sum}")


if __name__ == "__main__":
    main()
