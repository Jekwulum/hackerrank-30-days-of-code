"""
Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
"""



import math
import os
import random
import re
import sys

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    totalCost = meal_cost + tip + tax
    print(round(totalCost))

solve(meal_cost, tip_percent, tax_percent)
