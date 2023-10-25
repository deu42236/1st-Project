from time import sleep
import sys
container = 0
sleepDur = 0
gameRunning  = True


input("Welcome, choose you difficulty: Gentle (1), Mean (2), Troublesome(3), and Adorable(3): ")
print("You know what... It was completly useless. This game only has 1 difficulty")
print("Sorry for that. Good luck")
x = input("What's your name my friend? ")
print("OK, give me a second")
sleep(1)
if x.lower() == "krbec" or x.lower() == "jaroslav":
    print("GG, you won :)")
    sys.exit()
    #END 1
else:
    print("You know what... Nevermind.")
sleep(2)

print("INTRO")
print("\n\n Welcome to the game!\n \nYou have to walk through the labyrinth and find your way out. Along the way you will encounter various obstacles and puzzles that you must overcome. ")
sleep(7*sleepDur)
print("STORY:   One day you wake up in a dark room. You have no idea where you are or how you got there. All you know is that you have to find a way out.\nSTORY:   By feel, you'll find a flashlight to help you see in the dark.")
sleep(1*sleepDur)
print("STORY:   You turn on the light, and all you see is white.")
sleep(2*sleepDur)
print("STORY:   After a while you get used to the light and stand in the room. The walls are made of stone bricks, the only thing in the room is a 'bed'. Actually, it's a very cheap-looking mattress.")
sleep(2*sleepDur)
print("STORY:   You turn behind you, you see a door. A door with no handle. There's a hole in the door where it should be.")

print("Here comes your first decision: (1) You look out through the hole. (2) You run with all your might towards the door, thinking you're going to break it down.")

while gameRunning:
    dec = input("Your decision (1/2): ")
    if dec.lower() == "1":
        print("You put one eye to the hole. All you see is black. So you gonna try the door?")
        dec = input("Try it? (y/n)")
        if dec.lower() == "n":
            print("GAME OVER \n You stayed in the room until you died from lack of water. ")
            sys.exit()
            # END 2
        container = 1
    if dec == "2" or dec.lower() == "y":
        print("You rammed it into the door with all his might. You ripped the door open and found yourself in a huge hallway.")
        print("You find yourself in a dimly lit hallway. The walls are made of the same stone bricks as before. There are doors on both sides of the hallway.")
        print("Which door do you choose? (L) The door on the left. (R) The door on the right.")
        dec = input("Your decision (l/r): ")


    if dec.lower() == "l":
        print("You entered the room on the left. It's a small room with a single bed in it. The bed is unmade and there are some clothes on the floor.\n")
        print("You see a small window in the room. Do you want to investigate it? (y/n)")
        dec = input("Investigate the window? (y/n)")
        if dec.lower() == "y":
            print("You approach the window and see that the window leads to a balcony. You can see the city lights twinkling below you.")

            print("You open the window and climb out onto the balcony. You can see the city lights twinkling below you. You can also see a river flowing nearby.")
            print("Do you want to go back inside or keep exploring?")
            dec = input("Go back inside or keep exploring? (i/e): ")
            if dec.lower() == "i":
                print("You go back inside the room and close the window. You decide to rest for a while.")
                print("GAME OVER \n You stayed in the room until you died from lack of water. ")
                break
            elif dec.lower() == "e":
                print("You decide to keep exploring. You find a way down to the ground and start walking along the riverbank.")
                print("After a while, you come across a small hut. Do you want to investigate it? (y/n)")
                dec = input("Investigate the hut?(y/n) ")
                if dec.lower() == "y":
                    print("You approach the hut and find a small old man sitting outside. He seems friendly and offers you some water.")
                    print("Do you want to accept his offer? (y/n)")
                    dec = input("Accept the water? ")
                    if dec.lower() == "y":
                        print("You drink the water and feel refreshed. The old man tells you that he knows where you are, and he will hire you to his small cofee shop..")
                        print("You build up nice relationship with your chief, so you will eventually become kind of friends. One day, you will be free and manager of Mr Pavelka's coffee shop.")
                        print("\n\nCongratulations! You have won the game! You are working for an old man as a chashier in his store. But hey, you survived!")
                        sys.exit()
                        #END 3
                    elif dec.lower() == "n":
                        print("The old man hits you with a stick till you black out.")
                        print("When you wake up, you are in some coffee shop with strange band on your hand.")
                        print("The man told you, you are his slave now.")
                        dec = input("Do you want to resist? (y/n): ")
                        if dec.lower() == "y":
                            print("He taps a button on his desk and you receive a electric shock from the band. The old man just laught to you.")
                            print("Becouse you were not respecting me, I will send you to my coffee bean farm.")
                            print("GAME OVER \n you are now slave farming coffee for Mr. Pavelka")
                            sys.exit()
                            #END 4
                        elif dec.lower() == "n":
                            print("You build up nice relationship with your chief, so you will eventually become kind of friends. One day, you will be free and manager of Mr. Pavelka's coffee shop.")
                            sys.exit()
                            #END 3
                elif dec.lower() == "n":
                    print("You decide not to explore further.")
                    print("From the heaven falls big metal object, that you cannot identify.")
                    print("When it's getting closer, you see how big it is.")
                    print("You say: 'Jesus Christ on a motor bike! That is an enourmous giant fucking anvil.' you say out loud as it crushes you down into the ground")
                    print("GAME OVER \n You died, but it's coolest way to die. So it's kinda win, innit'.")
                    sys.exit()
                    #END 5

        elif dec.lower() == "n":
            print("You decided to walk out of this room and continue down the hallway.")
            dec = input("Do you want to investigate the second room? (y/n): ")
            if dec.lower() == "n":
                print("You continued down the hallway.")
                print("After about 5 minutes of walking, you see some guy.")
                print("You are happy to see some human after all that long time")
                print("You are shouting: 'Hey, where are we?")
                print("The guys doesn't see very friendly. He has both hands in pockets.")
                print("You explained that you are here, and you escaped from some really bad looking room")
                print("Suddenly the guy take his gun out, and start shouting at you.")
                print("He says: Stop right there. Don't make any sudden moves. One move and I'll shoot you fucking brain out")
                print("You accidentaly coughed, so he shoot your head with his Glock-17 Gen4")
                print("GAME OVER \n Your head has hole right through. (So you died BTW)")
                sys.exit()
                #END 6
    elif dec.lower() == "r":
        print("You can now see, why were this door opened.")
        print("There is pretty big hole under the toilet.")
        print("It's that big, that you could stuff yourself in there and get out.")
        print("But you don't know, what's on the second end of the hole")
        dec =input("Do you wanna risk it? (y/n):")
        if dec.lower() == "y":
            print("You took a deep breath and jumped into the hole.")
            print("And then you felt something hard against your backside.")
            print("Then you fell forward and hit your face against the ground.")
            print("You feel like you have been trampled by a herd of elephants.")
            print("GAME OVER \n You got crushed or stomped or whatever they do when they step on you.")
            sys.exit()
            #END 7
        elif dec.lower() =="n":
            print("You decided to stay away from the hole.")
            print("You walked around the corner, and found another door.")
            print("This one was locked, but you managed to crack the lock with your flashlight.")
            print("On the other side of the door, you saw a bright light.")
            print("You entered the room, and found yourself in a large, empty space.")
            print("In the center of the room, there was a table with candles.")
            print("They were lit, and their flames flickered in the dark air.")
            print("Around the table, there were people sitting in chairs.")
            print("All of them had eyes closed, and they seemed to be asleep.")
            print("One of them suddenly opens his eyes, looks at you, and smiles.")
            print("He says: 'Welcome to our home.'")
            print("You look around, trying to figure out who these people might be.")
            print("You noticed that everyone else seems to be blindfolded except for one person.")
            print("That person is holding a small knife, and he points it at you.")
            print("Everyone starts laughing.")
            print("Someone unblindfolds himself, revealing a man with a scar across his cheekbone.")
            print("He introduces himself as John Doe.")
            print("John explains that they are a group of survivors, and they need your help.")
            print("And when new guy appears, they need to fight the oldest member.")
            print("Oldest member is named Mr. Krbec.")
            print("Mr. Krbec is standing up, and he is not happy.")
            print("He shouts: 'I will kill you!')")
            print("John tries to calm him down, saying that you won't hurt anyone.")
            print("Mr. Krbece continues to rant about how you killed his family.")
            print("John tells you that you must defeat Mr. Krbec before anything happens.")
            print("You decide to go ahead and prepare for battle.")
            dec=input("Are you ready to fight? (y/n): ")
            if dec.lower()=="y":
                print("You charged towards Mr. Krbece, ready to kick some ass.")
                print("However, just as you reached him, you heard a loud noise behind you.")
                print("A massive creature emerged from the darkness, its eyes glowing red.")
                print("He said: 'Come'on JS, we've got some work to do.")
                print("The creature jumped on you, and smashed you to the ground.")
                print("GAME OVER \n You got eaten alive by the monster.")
                print("But there is the moral of the story. Never EVER try to fight Mr. Krbec")
            elif dec.lower() == 'n':
                print("You turn and run away from the danger.")
                print("As you run, you hear footsteps behind you.")
                print("Suddenly, you stop dead still.")
                print("There stands an old man, dressed in black robes.")
                print("He has a long white beard, and a staff in hand.")
                print("He says: 'Hello, young one. I see you're lost.")
                print("Follow me, and I may be able to guide you through this wilderness.")
                print("But remember: always trust those who wear black.")
                print("You noded your head, so you dont need to go back to the fight.")
                print("This guys seems to be lot stronger than your oponent Krbec")
                print("So you follow him into the unknown.")
                print("After ages of walking through the tunnel, you see light")
                print("You see some village.")
                print("The old man says: 'Now it's on you'")
                print("After a while, you come across a small hut. Do you want to investigate it? (y/n)")
                dec = input("Investigate the hut?(y/n) ")
                if dec.lower() == "y":
                    print("You approach the hut and find a small old man sitting outside. He seems friendly and offers you some water.")
                    print("Do you want to accept his offer? (y/n)")
                    dec = input("Accept the water? ")
                    if dec.lower() == "y":
                        print("You drink the water and feel refreshed. The old man tells you that he knows where you are, and he will hire you to his small cofee shop..")
                        print("You build up nice relationship with your chief, so you will eventually become kind of friends. One day, you will be free and manager of Mr. Pavelka's coffee shop.")
                        print("\n\nCongratulations! You have won the game! You are working for an old man as a chashier in his store. But hey, you survived!")
                        sys.exit()
                        #END 3
                    elif dec.lower() == "n":
                        print("The old man hits you with a stick till you black out.")
                        print("When you wake up, you are in some coffee shop with strange band on your hand.")
                        print("The man told you, you are his slave now.")
                        dec = input("Do you want to resist? (y/n): ")
                        if dec.lower() == "y":
                            print("He taps a button on his desk and you receive a electric shock from the band. The old man just laught to you.")
                            print("Becouse you were not respecting me, I will send you to my coffee bean farm.")
                            print("GAME OVER \n you are now slave farming coffee for Mr Krbec")
                            sys.exit()
                            #END 4
                        elif dec.lower() == "n":
                            print("You build up nice relationship with your chief, so you will eventually become kind of friends. One day, you will be free and manager of Mr. Pavelka's coffee shop.")
                            sys.exit()
                            #END 3