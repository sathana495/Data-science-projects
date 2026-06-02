#math module
import math as m
#Find the square root of a number.
print(m.sqrt(16))#its printing the square root of 16
#Calculate the factorial of 7.
print(m.factorial(7))#its printing the factorial of 7
#Find the value of π.
print(m.pi)#its printing the value of π
#Convert 180 degrees to radians.
print(m.radians(180))#its converting 180 degrees to radians
#Convert π radians to degrees.
print(m.degrees(m.pi))#its converting π radians to degrees
#Intermediate value of 10 and 20.
print(m.fsum([10, 20]))#its calculating the intermediate value of 10
#Find the GCD of 48 and 18
print(m.gcd(48, 18))#its printing the GCD of 48 and 18
#Find the LCM of 12 and 15.
def lcm(x, y):
    return (x * y) // m.gcd(x, y)
print(lcm(12, 15))#its printing the LCM of 12 and 15
#Find the ceiling and floor values of 15.7.
print(m.ceil(15.7))#its printing the ceiling value of 15.7
print(m.floor(15.7))#its printing the floor value of 15.7
#Calculate the distance between points (2,3) and (5,7)
def distance(x1, y1, x2, y2):
    return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  
print(distance(2, 3, 5, 7))#its calculating the distance between points (2,3) and (5,7)

#random module task
import random as r
#Generate a random number between 1 and 100.
print(r.randint(1, 100))#its generating a random number between 1 and 100
#Generate a random float.
print(r.uniform(1.0, 100.0))#its generating a random float between 1.0 and 100.0
#Pick a random fruit from a list
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print(r.choice(fruits))#its picking a random fruit from the list
#Toss a coin.
print(r.choice(['Heads', 'Tails']))#its tossing a coin and printing the result (Heads or Tails)
#Roll a dice.
print(r.randint(1, 6))#its rolling a dice and printing the result (a random number between 1 and 6)
#Generate a 6-digit OTP.
otp = ''.join([str(r.randint(0, 9)) for _ in range(6)])#its generating a 6-digit OTP by concatenating 6 random digits
print(otp)#its printing the generated OTP
#Create a random password of 8 characters.
import string
password = ''.join(r.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))#its creating a random password of 8 characters by concatenating random letters, digits, and punctuation
print(password)#its printing the generated password
#Shuffle a deck of cards.
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]#its creating a deck of cards by combining each rank with each suit
r.shuffle(deck)#its shuffling the deck of cards     
print(deck)#its printing the shuffled deck of cards
#Generate 10 random numbers and find the maximum.
random_numbers = [r.randint(1, 100) for _ in range(10)]#its generating a list of 10 random numbers between 1 and 100
print(random_numbers)#its printing the generated random numbers
print(max(random_numbers))#its printing the maximum value from the generated random numbers
#Generate 10 random numbers and find the maximum.
#pick 3 student name from a list of 10 student names
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
print(r.sample(students, 3))#its picking 3 random student names from the list of 10 student names

#Print the current working directory.
import os
print(os.getcwd())#its printing the current working directory
#Create a folder called "PythonPractice".
os.mkdir('PythonPractice')#its creating a folder called "PythonPractice"
#Check whether a folder exists.
print(os.path.exists('PythonPractice'))#its checking if the folder "PythonPractice" exists (True: exists, False: does not exist)
#rename the file
os.rename('PythonPractice', 'PythonPracticeRenamed')#its renaming the folder "PythonPractice" to "PythonPracticeRenamed"
#Delete the folder.     
os.rmdir('PythonPracticeRenamed')#its deleting the folder "PythonPracticeRenamed"