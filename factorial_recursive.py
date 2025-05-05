#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les entiers négatifs.")
    if n == 0:
        return 1
    return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Utilisation : python3 script.py <entier_positif>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    print(factorial(n))
except ValueError as e:
    print("Erreur :", e)
    sys.exit(1)