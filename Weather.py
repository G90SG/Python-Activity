# Create a program to ask the user the weather and advise them what clothing to take

#Assign weather variables 
raining = "a"
cold = "b"
fine = "c"
sunny = "d"
# Ask the user what the weather is like today
print ("What is the weather like today?")
weather = input("Is it (a) Raining  (b) Cold  (c) Fine (d) Sunny? ")

# Create an If statement to print a different sentence depending on the input received from the user 
if (weather == raining):
  print ("Don't forget an umbrella!")
elif (weather == cold):
  print ("Don't forget to take a coat!")
elif (weather == fine):
  print ("Lovely day for a walk!")
elif (weather == sunny):
  print ("Suns out Guns out! ")
else:
  print ("That isn't the answer I was looking for!")
