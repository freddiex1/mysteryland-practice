while True:



    locations = {
        "beach": ["jungle"],
        "jungle": ["beach", "cave"],
        "cave": ["jungle", "old bridge"],
        "old bridge": ["cave", "light house"],
        "light house": ["old bridge"]
    }

    location = "beach"
    inventory = []
    energy = 10


    while True:
        print()
        print(f"energy:{energy}")
        print(f"1 you look around the {location}(: ")
        print("2 what do you see")
        print("3 Move to another location")
        print("4 Quit")
        print("5 collect item")
        print("6 check inventory")
        print()

        choice = input("select action : ")

        if choice == "4":
            print()
            print("goodbye")
            break

        if choice not in ["1", "2", "3", "4","5", "6"]:
            print("Invalid option!")
            print("Please choose 1, 2, 3, 4, 5, or 6.")
            continue

        if choice == "2":
            print()
            print("you look around and see waves and palm trees.")

        if choice == "1":
            print()
            print(f"You take a closer look around the {location}.")

        if choice == "3":
            print()
            destination = input("where do you wanna go ?: ").lower()

            if destination in locations[location]:

                if destination == "old bridge" and "rope" not in inventory:
                    print("you need a rope to cross the bridge!")

                else:
                    location = destination
                    energy -= 1
                    print()
                    print(f"you are now at {location}")
            else:
                print("you cant move there!")


            if energy == 0:
                print()
                print("game over! you ran out of energy")
                break


            if location == "light house":
                if "rope" in inventory and "lantern" in inventory:
                    print()
                    print("congratulations! you won!")
                    break

        if choice == "5":

            if location == "beach":
                if "rope" not in inventory:
                    inventory.append("rope")
                    print("You collected the rope")
                else:
                    print("You already have the rope!")


            if location == "cave":
                if "lantern" not in inventory:
                    inventory.append("lantern")
                    print("you have collected the lantern")
                else:
                    print("you already have lantern")

            if location != "beach" and location != "cave":
                print("there is nothing here to collect!")

        if choice == "6":
            if not inventory:
                    print("your inventory is empty.")
            else:
                print(f"your inventory: {inventory}")

    while True:
        print()
        print("would you like to play again")
        print("1. yes")
        print("2. no")

        replay = input("choose: ").lower()

        if replay == "1":
            break

        if replay == "2":
            print()
            print("Thanks for playing!")
            exit()

