print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----|
 \_/__________________________________________________________________|
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     ||//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //|| " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    |"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------|
 \_/__________________________________________________________________|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You dock your boat at the island your treasure map has lead you to. There is an abandoned boat there as well.")
choice1 = input("Do you go LEFT and check out the boat or RIGHT to go up the dock to explore the island? L or R ").lower()
if choice1 == "l":
    print("You climb aboard the abandoned boat and open the door to get into the bridge.  A skeleton drives a sword right through your chest and you die.")
    print("GAME OVER!")
elif choice1 == "r":
    print("You walk up the dock and just past the large, rocky seawall you see a cabin.")
    choice2 = input("Do you go LEFT and walk deeper into the island or RIGHT to go into the cabin? L or R ").lower()
    if choice2 == "l":
        print("You attempt to climb over more rocks to get a better view of the island and lose your grip. You tumble down the rocks and smash your head and die.")
        print("GAME OVER!")
    elif choice2 == "r":
        print("You open the front door of the cabin and slowly walk in. You look around but see nothing except a cracked open door with a faint sound of music coming from the darkness.")
        choice3 = input("Do you go BACK and run to your boat, terrified, and leave the island or do you go STRAIGHT and open the door? B or S ").lower()
        if choice3 == "s":
            print("You slowly open the door, allowing the music to get louder. You turn on a flashlight and walk down the stairs. At the bottom, you start to open the door and as the door cracks open, a bright light starts shining through.")
            choice4 = input("Do you go BACK and run up the stairs, out of the cabin and back to your boat or do you go STRAIGHT and continue opening the door? B or S ").lower()
            if choice4 == "s":
                print("You open the door, the soft melody gets louder and you are nearly blinded by the amount of gold and treasure you have found. You celebrate and grab as much as you can and carry it back to your boat.")
                print("CONGRATULATIONS! YOU WIN!!")
            elif choice4 == "b":
                print("You turn around to run back up the stairs and out of the cabin to your boat. As you leave the cabin running, you trip on a rock, smash your head and die.")
                print("GAME OVER!")
            else:
                print("You turn around to run up the stairs, slip and fall through the door. The fall breaks your neck and you slowly die, looking at the treasure you could have had if you weren't such a chicken.")
                print("GAME OVER!")
        elif choice3 == "b":
            print(
                "You turn around to run back to your boat but trip over your feet and land on a sword, priercing your heart and die slowly.")
            print("GAME OVER!")
        else:
            print("Terrified, you turn around to run back to your boat without any treasure.")
            print("GAME OVER!")
    else:
        print("You are too scared and turn around to run back to your boat without the treasure.")
        print("GAME OVER!")
else:
    print("You slip off the dock, smash your head on a rock and die.")
    print("GAME OVER!")

