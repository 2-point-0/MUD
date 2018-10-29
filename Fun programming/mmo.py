import random
import pyttsx3
import classes 

engine = pyttsx3.init()

play_again = "y"
while play_again == "y":
# character selection

    engine.say(", Choose your class")
    print("Choose your class:")

    print("")

    engine.say("Mage")
    print("Mage")
    print("The stats for Mage are:")
    print("Intellegence:6")
    print("Accuracy:5")
    print("Strength:1")
    print("Stealth:3")
    print("Dexterity:3")
    print("Luck:4")

    print("")

    engine.say("Soldier")
    print("Soldier")
    print("The stats for Soldier are:")
    print("Intellegence:1")
    print("Accuracy:3")
    print("Strength:8")
    print("Stealth:1")
    print("Dexterity:5")
    print("Luck:3")

    print("")

    engine.say("Assassin")
    print("Assassin")
    print("The stats for Assassin are:")
    print("Intellegence:1")
    print("Accuracy:4")
    print("Strength:2")
    print("Stealth:6")
    print("Dexterity:4")
    print("Luck:5")

    engine.runAndWait()

    print("")

    clas = input("").lower()

    while clas != "Fals":
        if clas == "mage":
            stats = classes.stats.mage
            break
        if clas == "soldier":
            stats = classes.stats.soldier
            break
        if clas == "assassin":
            stats = classes.stats.assassin
            break
        else:
            engine.say("You selected an invalid class please enter a vaild class")
            print("You selected an invalid class please enter a vaild class")
            engine.runAndWait()
            clas = input("").lower()

    print("")

    engine.say("You selected %s" % clas)
    print("You selected", clas)
    engine.runAndWait()

    print("")


    #Mage start
    if clas == "mage":
        classes.mage()

    #Soldier and Assassin start
    if clas == "soldier":
        classes.soldier()
    if clas == "assassin":
        classes.assassin()
        
    engine.say("Do you want to play again yes or no:")
    engine.runAndWait()
    play_again = input("Do you want to play again y/n:")
    
    
