# ZEN =  Zion Kinniebrew-Jenkins (Author)
# Zion Kinniebrew-Jenkins
# 02/18/2025
def display_map(rooms):
    """
    Display the full map of the DC Universe.
    Note: Viewing the map will impose a penalty to your score.
    """
    print("\nFull Map of the DC Universe:")
    for room, details in rooms.items():
        print(f"{room}:")
        for key, value in details.items():
            if key in ['North', 'South', 'East', 'West']:
                print(f"  {key} -> {value}")
            elif key == 'Item':
                print(f"  Contains item: {value}")
            elif key == 'Villain':
                print(f"  Contains villain: {value}")

def display_inventory(inventory):
    """
    Display the player's current inventory in a formatted manner.
    """
    print("\nYour current inventory:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("  (empty)")

def bonus_level(score):
    """
     The bonus level in Hueco Mundo (虚圏ウェコムンド),
    where the player teams up with Ichigo to defeat Aizen.
    If the player wins the bonus battle, they are transferred to the final winning screen.
    """
    print("\n*** Bonus Level: Hueco Mundo (虚圏ウェコムンド) ***")
    print("You have teamed up with Ichigo to defeat Aizen!")
    aizen_health = 30
    while aizen_health > 0:
        cmd = input("Type 'attack' to strike Aizen: ").lower()
        if cmd == "attack":
            aizen_health -= 10
            print(f"You attacked Aizen! Remaining health: {aizen_health}")
        else:
            print("Invalid command in battle! Please type 'attack'.")
    # Award bonus points for defeating Aizen
    bonus_points = 50
    score += bonus_points
    print(f"\nAizen has been defeated! You have earned an additional {bonus_points} bonus points.")
    print("\n" + "*" * 40)
    print(" " * 10 + "WINNER!")
    print("*" * 40)
    print(f"Your final score is: {score}")
    return score

def main():
    # Define the game map: rooms with directional links, items, and villains.
    rooms = { 
        'Gotham City Streets': {
            'North': 'Wayne Tower', 
            'East': 'Arkham Asylum', 
            'South': 'Metropolis Museum', 
            'West': "Harley's Hideout"
        },
        'Wayne Tower': {
            'South': 'Gotham City Streets', 
            'East': 'Gotham Museum', 
            'Item': 'Batarang'
        },
        'Gotham Museum': {
            'West': 'Wayne Tower', 
            'Item': 'Ancient Egyptian Amulet'
        },
        'Arkham Asylum': {
            'West': 'Gotham City Streets', 
            'Item': 'Joker Venom Vial'
        },
        'Metropolis Museum': {
            'North': 'Gotham City Streets', 
            'East': 'S.T.A.R. Labs', 
            'Item': 'Kryptonite Shard'
        },
        'S.T.A.R. Labs': {
            'West': 'Metropolis Museum', 
            'East': "Joker's Hideout", 
            'Item': "Metallo's Power Core"
        },
        "Joker's Hideout": {
            'West': 'S.T.A.R. Labs', 
            'Villain': 'The Joker'
        },
        "Harley's Hideout": {
            'North': "Poison Ivy's Apartment", 
            'East': 'Gotham City Streets', 
            'Item': "Harley Quinn's Mallet"
        },
        "Poison Ivy's Apartment": {
            'South': "Harley's Hideout"
        }
    }
    
    # List of required items that must be collected to defeat the villain.
    required_items = [
        'Batarang', 
        'Ancient Egyptian Amulet', 
        'Joker Venom Vial', 
        'Kryptonite Shard', 
        "Metallo's Power Core", 
        "Harley Quinn's Mallet"
    ]
    
    # Initialize game state variables.
    current_room = 'Gotham City Streets'
    inventory = []
    visited_rooms = set()
    score = 0
    bonus_level_unlocked = False
    
    # Mapping for single-key directional commands.
    direction_map = {
        'n': 'North',
        's': 'South',
        'e': 'East',
        'w': 'West'
    }
    
    # Validate and obtain player's name.
    while True:
        player_name = input("Welcome to the DC Comics Game! Please enter your name: ")
        if player_name.strip():
            break
        else:
            print("Invalid name. Please enter a name (not just spaces).")
    
    print(f"\nWelcome, {player_name}! Get ready to explore the DC Universe.")
    print("Created by ZEN")
    
    # Main gameplay loop.
    while True:
        # Award points for visiting a new room.
        if current_room not in visited_rooms:
            visited_rooms.add(current_room)
            score += 10
            print(f"\n[Points +10] You have earned 10 points for visiting {current_room}.")
        
        print("\n------------------------------")
        print(f"You are in {current_room}")
        print("Inventory:", inventory)
        print(f"Current Score: {score}")
        
        # Check if the player has encountered the villain.
        if 'Villain' in rooms[current_room]:
            if all(item in inventory for item in required_items):
                # If bonus level was unlocked via secret code, transfer to bonus level.
                if bonus_level_unlocked:
                    print("\nSecret code detected! You are being transferred to the bonus level: Hueco Mundo!")
                    current_room = "Hueco Mundo"
                    score = bonus_level(score)
                    break
                else:
                    print("\nCongratulations! You have collected all items and defeated The Joker!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    print(f"Your final score is: {score}")
                    break
            else:
                print("\nNOM NOM...GAME OVER!")
                print("Thanks for playing the game. Hope you enjoyed it.")
                print(f"Your final score is: {score}")
                break
        
        # Special case: Bonus level room Hueco Mundo is handled separately.
        if current_room == "Hueco Mundo":
            score = bonus_level(score)
            break
        
        # If an item is present in the room, prompt the player to pick it up.
        if 'Item' in rooms[current_room]:
            item = rooms[current_room]['Item']
            print(f"You see a {item} here.")
            take_item = input("Do you want to pick it up? (yes/no): ").lower()
            if take_item == 'yes':
                inventory.append(item)
                score += 20
                print(f"[Points +20] You picked up {item} and earned 20 points!")
                del rooms[current_room]['Item']
        
        # Display the available exits based on the room's directional keys.
        print("\nAvailable exits:")
        for direction in rooms[current_room]:
            if direction in ['North', 'South', 'East', 'West']:
                print(f"- {direction} ({direction[0].lower()})")
        
        # Prompt the player for their next command.
        command = input("\nEnter a direction (N/S/E/W), 'map' to view the map, 'inventory' to view your items, 'exit' to quit, or enter secret code: ").lower()
        
        # Process the player's command.
        if command == 'exit':
            print("\nThanks for playing! Goodbye for now.")
            print("Created by ZEN")
            break
        elif command == 'map':
            print("\nWarning: Viewing the map will expose your upcoming adventures. Nothing good ever comes easy; you will be penalized for this action.")
            confirm = input("Are you sure you want to view the full map? (yes/no): ").lower()
            if confirm == 'yes':
                score -= 15
                print("[Points -15] You have been penalized 15 points for viewing the map.")
                display_map(rooms)
            continue
        elif command == 'inventory':
            display_inventory(inventory)
            continue
        elif command == "0032":
            bonus_level_unlocked = True
            print("\nSecret code accepted! Bonus level unlocked. Defeat The Joker and you will be transported to Hueco Mundo for an epic bonus challenge!")
            continue
        # If the command is a single-letter direction.
        elif command in direction_map:
            desired_direction = direction_map[command]
            if desired_direction in rooms[current_room]:
                current_room = rooms[current_room][desired_direction]
            else:
                print("You can't go that way.")
        # If the command matches a full direction name.
        elif command.capitalize() in rooms[current_room]:
            current_room = rooms[current_room][command.capitalize()]
        else:
            print("Invalid command. Please enter a valid direction (N/S/E/W), 'map', 'inventory', 'exit', or a secret code.")
    
if __name__ == "__main__":
    main()
