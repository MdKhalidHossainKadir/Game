from time import sleep # for make the delay of output
from sys import exit

print("Loading.....")
sleep(2)

print("Looking for updates .....____.....")
sleep(3)

print("Welcome to the Home Work Game!!!")
print("Now, you're in the front door of a mysterious house!!🥶☠️👻")
 
enter = input("type enter to enter in the house \n> ")

def approch(room_number):
    print(f"Approching  towards the door - {room_number}")
    sleep(5)
    print("You start knocking the door.....")
    for knock in range (0,3):
        print("knock  ")
        sleep(2)

def enter_cd():
    if enter == "enter":
        print("Great! You're now in the house. ")
        print("Looking for somethings in the dark...")
        sleep(4)
    else:
        print("Follow the command or stay out side the house. LOL!!") 
          
def ground_floor():
    print("There is a vage image infront of you ...")
    sleep(3)
    print("You found three rooms here..")
    go = input("Which one you want to enter?\n>")
    if go == "1":
       approch(go)
       print("No one respond... ")
       sleep(3)
       print("You try to open the door, but it is locked")

    
    
    elif go == "2":
        approch(go)
        print("The door open slightly by the hit of knocking..")
        sleep(3)
        print("And you see a big tiger movig round and round in the room...")
        print("What you do now?..")
        action = input(" > ")
        if action == "keep quit":
            print("great choice, Now silently close the door. ")

        elif action == "make sound":
            print("The tiger eating you body.")

        else:
            print("The tiger saw you ......")

    elif go == "3":
        approch(go)
        sleep(3)
        print("The door openned automaticly")
        print("This room is full of snakes.")


def First_floor():
    print("Everything is fridged.")
    sleep(2)
    print("Some thing is counting down...")
    for count in range(0,10):
        print(count)
        sleep(1)
    
    print("The solders are start moving... ")
    action = input("What will you do now? \n >")
    
    if action == "hide" or action == "seek for shelter":
        print("Great , you may leave this alive.")
        print("You escaped alive")

    elif action == "run":
        print("A solder shot at you and you are dead..")

    else:
        print("You are hit by a granade..BOOM<")


def Second_floor():
    approch(False)
    print("The door opend...")
    sleep(6)
    print("You're just amazed the this floor is full of wonders.")
    print("It's a cyberpunk city here...")

def tarrce():
    print("The tarrce is full of Zoombie !!")
    action = input("What will you do now ? \n >")
    if action == "run back" :
        print("The Zoombies are chasing you....")
        print("You strumble and fall in the floor they eat you.!!!")

    elif action == "jump from the building":
        print("You hit the ground badly and your body split into pices")

    else:
        print("one of the Zoombie bite you and you turned into a Zoombie too!!")


def main():
    enter_cd()
    decision = input("Which floor you want to explore?? \n >")

    if decision == "0" or decision =="ground floor":
        ground_floor()

    elif decision == "1" or decision == "first floor":
        First_floor()
    
    elif decision == "2" or decision == "second floor":
        Second_floor()

    elif decision == "3" or decision == "tarrce":
        tarrce()

    else:
        print("Enter proper floor name or number..")    
       
main()