#!/usr/bin/env python3
# ------------------------------------------------- #
# Secure Multi-Party Computation
# Implementation of Secure Summation with n Parties
# ------------------------------------------------- #
from party import Party

# Settings
N = 100  # threshold
M = 0  # 'uninitialized' modulo
parties = []

try:
    n = int(input("How many Parties would you like to create: "))
    if(n <= 2):
        raise Exception("Error! Please create more than 2 Parties.")
    else:
        # Initialize modulo
        M = n * N

        # Create parties
        print("\n---------- Creating {} Parties ----------\n".format(n))
        for i in range(0, n):
            parties.append(Party("Party_" + str(i), int(
                input("Enter a secret value for Party_{}: ".format(i))
                ), n, M))

        # Secret sharing
        for i in range(0, n):
            for j in range(0, n):
                parties[j].giveRandomValue(parties[i].getRandomValue(j))

        # Share column sums
        for i in range(0, n):
            for j in range(0, n):
                parties[i].giveColumnSum(parties[j].getColumnSum())

        # Validate function output
        print("\n---------- Computing Common Function f(x) ----------\n")
        for i in range(0, n):
            print("{} has computed f(x) = {}".format(
                parties[i].name, parties[i].calculateF()))
except ValueError:
    print("Invalid input! Please enter a valid integer.")
