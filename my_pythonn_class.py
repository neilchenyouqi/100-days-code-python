# this is my python class
import random
computerrps = "start"
computerchoice = str(random.randint(1 ,3))
if computerchoice == "1":
    computerrps = "rock"
elif computerchoice == "2":
    computerrps = "paper"
elif computerchoice == "3":
    computerrps = "scissors"

print(computerrps)