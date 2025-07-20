import random as rd
import time
import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import os
import sys
import json
import requests
import datetime
import math
import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# This is a simple number guessing game where the user has to guess a number between 1 and 100.

def start_game():
    print("""welcome to the game
    I am gussing a number between 1 to 100!
    You have 5 chances to guess the correct number.
        Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)

    """)

def main():
    random_number = rd.randint(1, 100)
    start_game()
    choice = input("Enter your choice: ")
    start_time = time.time()
    if choice == '1':
        for i in range(10):
            guess = int(input("enter your guess: "))
            if guess == random_number:
                print(f"nice job,you guessed the number in {i + 1} tries!")
                break
            elif random_number > guess:
                if i + 1 == 10:
                    print("you lost!")
                else:    
                    print("the number is greater than your guess")
            elif random_number < guess:
                if i + 1 == 10:
                    print("you lost!")
                else:    
                    print("the number is smaller than your guess")
                print("the number is smaller than your guess")
        #print("you lost!")
    elif choice == '2':
        for i in range(5):
            guess = int(input("enter your guess: "))
            if guess == random_number:
                print(f"nice job,you guessed the number in {i + 1} tries!")
                break
            elif random_number > guess:
                if i + 1 == 5:
                    print("you lost!")
                else:    
                    print("the number is greater than your guess")
            elif random_number < guess:
                if i + 1 == 5:
                    print("you lost!")
                else:    
                    print("the number is smaller than your guess")
        #print("you lost!")
    elif choice == '3':
        for i in range(3):
            guess = int(input("enter your guess: "))
            if guess == random_number:
                print(f"nice job,you guessed the number in {i + 1} tries!")
                break
            elif random_number > guess:
                if i + 1 == 3:
                    print("you lost!")
                else:    
                    print("the number is greater than your guess")
            elif random_number < guess:
                if i + 1 == 3:
                    print("you lost!")
                else:    
                    print("the number is smaller than your guess")
        #print("you lost!")
    
    else:
        print("invalid!please choose 1 or 2 or 3.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    #timer()
    play_again()

def play_again():
    Play_again = input("""do you wanna play again?
          y.yes
          n.no  
          """)
    if Play_again == 'y':
        main()
    else:
        print("goodbye!")

if __name__ == "__main__":
    main()      