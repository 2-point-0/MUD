import pyttsx3
engine = pyttsx3.init()
def mage():
    engine.say("You wake up in a dark cave with nothing but the clothes on your back and the spells you have learned over the years. What will you do now?")
    print("You wake up in a dark cave with nothing but the clothes on your back and the spells you have learned over the years. What will you do now?")

    print("")
        
#First section of options for mage
    engine.say("Try to find the entrance to the cave, Try going deeper into the cave, or look around the cave?")
    print("Find entrance")
    print("Go deeper")
    print("Look around")
    engine.runAndWait()
