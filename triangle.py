#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Nov 2022
# This program converts temperature

import random


def area_triangle(int_base, int_height):
    # calculate area

    # process
    area = int_base * int_height / 2

    # output
    print("The area is: {0}".format(area))


def main():
    # input
    print("This program calculates the area of a triangle.")
    str_base = input("Enter base of triangle: ")
    str_height = input("Enter height of triangle: ")

    try:
        int_base = int(str_base)
        int_height = int(str_height)
        # call functions
        area_triangle(int_base, int_height)
    except ValueError:
        print("Invalid integer")

    print("\nDone.")


if __name__ == "__main__":
    main()
