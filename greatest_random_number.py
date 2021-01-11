#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021
# This program finds the greatest number in a list of random numbers

import random


def greatest_finder(numbers):
    # This program finds the greatest number in a list of random numbers

    previous_greatest_number = 0

    for loop_counter in range(0, 10):
        if previous_greatest_number < numbers[loop_counter]:
            previous_greatest_number = numbers[loop_counter]
    return previous_greatest_number


def main():
    # This function generates 10 random numbers and displays them

    numbers = []
    sum_of_numbers = 0

    print("The following is 10 randomly generated numbers"
          " stored in the same variable.")
    print("")

    for loop_counter in range(0, 10):
        a_single_random_number = random.randint(0, 100)
        numbers.append(a_single_random_number)

    for loop_counter in range(0, 10):
        print("Random number {0}: {1}".format(loop_counter + 1,
                                              numbers[loop_counter]))

    greatest_number = greatest_finder(numbers)

    print("")
    print("The highest one is {0}".format(greatest_number))
    print("")


if __name__ == "__main__":
    main()
