# Create a program to ask the user their name, ask them guess the number I am thinking of between 1 and 10

# Import random module
import random
# Say Hello and get the users name
myName = input ("Hello! What is your name? ")
# Assign the variable 'number' to a random integer between 1 and 10
number = random.randint(1,10)
# Tell the user I am thinking of a number between 1 and 10
print (myName + ", I am thinking of a number between 1 and 10.")
# Take the guess from the users keyboard input 
guess = int(input( "Take a guess: "))
if guess == number: 
  print("Good job, " + myName + "! You guessed my number.")
if guess != number:
  print ("Better luck next time.")
