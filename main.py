# John Elehwany and Owen Sanchez
# Loyola CompSci 151
# Professor Zee
# Lab: 08

# This program simulates rolling a pair of six-sided dice a number of times dependent on the user, and then it displays the results of the number of rolls.

import random

def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

num_rolls = int(input("How many times would you like to roll? "))

for i in range(num_rolls):
    dice1, dice2 = roll()
    total = dice1 + dice2
    print(f'You rolled {dice1} and {dice2}.` Your total is {total}')