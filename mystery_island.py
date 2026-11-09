# ======== GAME DATA ========
locations = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]
# =======PLAYER STATUS FUNCTION=======
def show_player_status(name, location, energy, has_rope, has_lantern):
    print("===== PLAYER STATUS =====")
    print(f"Player: {name}")
    print(f"Current location: {location}")
    print(f"Remaining energy: {energy}")
    print(f"Has rope: {has_rope}")
    print(f"Has lantern: {has_lantern}")
# ========MOVEMENT FUNCTION========

def move_player(current_location, destination, energy, locations, has_rope, has_lantern):

    if destination not in locations:
        print("Invalid destination!")

    elif energy <= 0:
        print("You have no energy left!")

    elif destination == "Old Bridge" and not has_rope:
        print("You need a rope to cross the Old Bridge!")

    elif destination == "Lighthouse" and not has_lantern:
        print("You need a lantern to enter the Lighthouse!")

    else:
        energy -= 1
        current_location = destination
        print(f"You have moved to {current_location}!")
        print(f"You have {energy} energy remaining!")

    return current_location, energy


def light_lighthouse(current_location, has_lantern):

    if current_location == "Lighthouse" and has_lantern:
        return "Congratulations! You have completed your mission!"

    else:
        return "You need to reach the Lighthouse with a lantern!"

# =========INSTRUCTIONS=========
def show_instructions():
    print("======GAME INSTRUCTIONS=====")
    print("You start at the Beach with 5 energy points.")
    print("Collect the rope in the Jungle.")
    print("Collect the lantern in the Cave.")
    print("You need the rope to cross the Old Bridge.")
    print("You need the lantern to enter the Lighthouse.")
    print("Reach the Lighthouse with your lantern to win.")

# ========START ADVENTURE========
def start_adventure():
    current_location = "Beach"
    energy = 5
    has_rope = False
    has_lantern = False
    player_name = input("Enter your name: ").strip().title()

    print(f"Welcome! You are starting at {current_location}.")
    print("Your adventure is beginning!")

    while True:

        if energy == 0:
            print("You have run out of energy!")
            print("GAME OVER!")
            break

        choice = input("Enter a destination or type quit: ")
        choice = choice.strip().title()

        if choice == "":
            print("Please enter a destination or type quit.")
            continue

        if choice == "Quit":
            print("Thanks for playing!")
            break

        else:
            new_location, new_energy = move_player(
                current_location,
                choice,
                energy,
                locations,
                has_rope,
                has_lantern
            )

            current_location = new_location
            energy = new_energy

            if current_location == "Jungle" and not has_rope:
                has_rope = True
                print("Congratulations! You have collected the rope!")

            if current_location == "Cave" and not has_lantern:
                has_lantern = True
                print("Congratulations! You have collected the lantern!")

    
            show_player_status(
                player_name,
                current_location,
                energy,
                has_rope,
                has_lantern
            )
    
            if current_location == "Lighthouse":
                result = light_lighthouse(current_location, has_lantern)
                print(result)
                break

    
            if energy == 0:
                print("You have run out of energy!")
                print("GAME OVER!")
                break


# ========MAIN MENU========

def main():
    choice = ""

    while choice != "3":
        print("===== MAIN MENU =====")
        print("1. Start Adventure")
    
        print("2. View Instructions")
        print("3. Quit Game")

        choice = input("Enter your choice: ")

        if choice.strip() == "":
            print("Please enter 1,2,or 3.")
            continue

        if choice == "1":
            start_adventure()
        elif choice =="2":
            show_instructions()
        elif choice == "3":
            print("Goodbye!")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()