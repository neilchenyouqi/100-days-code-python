#IMPORTANT: Add a "" around the input

#Day 1: Band name generator(V1)
print("Band Name Generator")
city = input("What is the name of the city you grew up in?")
animal = input("What is your favourite animal?")
print("Your band name could be " + city + " " + animal)

#Day 1(V2)
print("Band name generator")
print("Your band name could be " + input("What is the name of the city you grew up in?") + " " + input("What is the name of your favourite animal?"))

#Side Project: Passcode Lock
factor = True #initialize
c = 0
tries = 3
#Change the variable underneath this for more or less tries.
triesleft = 3
#You can change the variable underneath this for different passwords.
yourpassword = 2345

while factor == True:
    #Remember to change this if you have changed your password.
    guess = input("What is the passcode? Hint: It's 4 digits long.\n")
    
    if yourpassword == guess and triesleft >> 3:
        print("Congratulations! You may enter.")
        print("You made it through with "+ str(triesleft) + " tries left!")
        break

    if yourpassword == guess and triesleft << 3:
        print("Congratulations! You may enter.")
        print("You made it through with "+ str(triesleft) + " tries left!")
        break

#Change the part below if you have changed the amount of tries.
    if yourpassword == guess and triesleft == 3:
        print("Congratulations! You may enter.")
        print("You made it through without failing once! Good job!")
        break

              
    if yourpassword >> guess and c < tries:
        print("Wrong! Try again.")
        triesleft = triesleft - 1
        print("You have " + str(triesleft) + " tries left.")
        c = c + 1

    if yourpassword << guess and c < tries:
        print("Wrong! Try again.")
        triesleft = triesleft - 1
        print("You have " + str(triesleft) + " tries left.")
        c = c + 1

    if c == tries:
        print("Wrong! Sorry, you've ran out of tries.")
        factor = False
#Day 2: Tip Calculator(probably not the most efficent)
print("Welcome to the tip calculator!\n")
first_bill = input("What was the total bill?\n")
tip_percentage = input("How much would you like to tip? 10, 12 or 15?\n")
people_split = input("How many people are splitting the bill?\n")
timestip = (int(first_bill) * (int(tip_percentage) / 100)) + int(first_bill)
aftersplit = round(timestip / int(people_split), 2)
print("Each person will pay " + str(aftersplit))
#Day 3: Treasure Island(Choose your own adventure)
#EDIT THE STORY TO YOUR LIKING
factor = True
while factor == True:
    print("Welcome to Treasure Island! Your mission is to find the treasure.")
    whichway = input("You come to a crossroads. Which way do you go, left or right?\n")
    if whichway == "right":
        print("You fell into a hole. Game Over.")
        factor = False
    elif whichway == "left":
        print("You've come to a lake. There is an island in the middle of the lake.")
        lakechoice = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
        if lakechoice == "wait":
            door = input("You've gotten to the island unharmed. There is a house with 3 doors; red, yellow and blue. Which one do you go into?\n")
            if door == "red":
                print("You enter a room full of fire. Game Over.")
                factor = False
            elif door == "blue":
                print("You enter a room full of beasts. Game Over.")
                factor = False
            elif door == "yellow":
                print("You've found the treasure! Congratulations!")
                factor = False
        else:
            print("You get attacked by an angry trout. Game Over.")
            factor = False
#Day 4: Rock paper scissors
import random
computerrps = "start"
print("Welcome to Rock Paper Scissors")
playerchoice = input("Choose rock, paper or scissors\n")
computerchoice = str(random.randint(1, 3))
if computerchoice == "1":
        computerrps = "rock"
elif computerchoice == "2":
       computerrps = "paper"
elif computerchoice == "3":
       computerrps = "scissors"

if computerrps == "rock" and playerchoice == "rock":
        print("The computer chose rock. It's a tie!")
elif computerrps == "rock" and playerchoice == "paper":
        print("The computer chose rock. You win!")
elif computerrps == "rock" and playerchoice == "scissors":
        print("The computer chose rock. You lose!")
elif computerrps == "paper" and playerchoice == "scissors":
        print("The computer chose paper. You win!")
elif computerrps == "paper" and playerchoice == "paper":
        print("The computer chose paper. It's a tie!")
elif computerrps == "paper" and playerchoice == "rock":
        print("The computer chose paper. You lose!")
elif computerrps == "scissors" and playerchoice == "scissors":
        print("The computer chose scissors. It's a tie!")
elif computerrps == "scissors" and playerchoice == "paper":
        print("The computer chose scissors. You lose!")
elif computerrps == "scissors" and playerchoice == "rock":
        print("The computer chose scissors. You win!")