import time


def scene_one():
    print("Welcome to the second version of 'The coffin of Ansy and Ashley' made by anikiwii")
    print("You arrive to the basement and you see Mrs. Graves, who really wants to tell you something.")
    print("Mrs. Graves: Andy, we need to talk. Sit down, please.")

    choice = input("1. Sit down and listen\n2. Refuse to listen and start the ritual.\n")

    if choice == '1':
        scene_two()
    elif choice == '2':
        print("You start the ritual as soon as Ashley arrives. Mrs. Graves in tears. *Game continues as always.*")


def scene_two():
    print("Mrs. Graves reveals that you are adopted, leaving you stunned.")
    print("Mrs. Graves: I've loved you as my own, Andy. Nothing changes between us.")

    choice = input("1. Express gratitude for her honesty. You just wonder why you were treated this way for years. "
                   "After all, if they adopted you, it means they wanted you. Yes...?\n2. Feel even more betrayed and "
                   "demand more answers. Start"
                   "the ritual with Ashley. *Game continues as always.*\n")

    if choice == '1':
        scene_three()
    elif choice == '2':
        print("You demand more answers, causing tension in the conversation.")


def scene_three():
    print("Distraught, you decide to take some time. But the ritual needs to be done!!!")
    print("You are confused, you walk through the house. Upstairs you meet Ashley, your sister, who has always been "
          "'supportive.', if you know what I mean.")

    choice = input("1. Open up to Ashley about the revelation.\n2. Keep the secret and avoid the topic\n")

    if choice == '1':
        scene_four()
    elif choice == '2':
        print("You keep the secret, distancing yourself from Ashley. The ritual begins.")


def scene_four():
    print("As you spend more time with Ashley, your secret feelings for her resurface.")
    print("You start to question the meaning of family, bit you also know that you can finally express your feelings "
          "to her, as she isn't your sister 'anymore'.")

    choice = input("1. Confess your feelings to Ashley\n2. Keep your feelings a secret.\n")

    if choice == '1':
        scene_five()
    elif choice == '2':
        print("You keep your feelings a secret. The ritual begins.")


def scene_five():
    print("You confront Mrs. Graves to discuss your feelings and seek closure.")
    print("Your choices throughout the game will impact the ending.")

    choice = input(
        "1. Choose to pursue a romantic relationship with Ashley\n2. Take time for yourself. There are more problems "
        "now.\n")

    if choice == '1':
        print("Congratulations! You chose to pursue a romantic relationship with Ashley. ")
    elif choice == '2':
        print("Congratulations! You chose to take time for yourself, you need to do the ritual. ")
    else:
        print("Invalid choice. Game over.")

# Start the game
scene_one()
