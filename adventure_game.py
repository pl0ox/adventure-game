import time
import random

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("Welcome to the Adventure Game!")
    print_pause("You find yourself in a mysterious forest.")
    print_pause("Your mission is to find the hidden treasure.")
    print_pause("Be careful, danger lurks in every corner.")

def explore_forest(total_score):
    print_pause("You start exploring the forest.")
    print_pause("As you walk, you hear strange sounds and see peculiar creatures.")
    print_pause("Suddenly, you stumble upon an old tree with a hidden door.")
    print_pause("Do you want to open the door? (1) Yes (2) No")
    choice = input()
    if choice == '1':
        print_pause("You open the door and find a chest filled with gold and jewels!")
        print_pause("Congratulations! You have found the hidden treasure. You are victorious!")
        total_score += 10
    elif choice == '2':
        print_pause("You decide not to open the door and continue exploring.")
    else:
        print_pause("Invalid input. Please enter 1 or 2.")
        return explore_forest(total_score)
    return total_score

def encounter_enemy(total_score):
    print_pause("As you venture deeper into the forest, you encounter a fearsome enemy.")
    print_pause("The enemy challenges you to a duel.")
    print_pause("Do you want to fight? (1) Yes (2) No")
    choice = input()
    if choice == '1':
        outcome = random.choice(['win', 'lose'])
        if outcome == 'win':
            print_pause("You defeat the enemy and continue your journey.")
            total_score += 5
        else:
            print_pause("The enemy overwhelms you. You lose the battle.")
            print_pause("Game over!")
            total_score -= 5
    elif choice == '2':
        print_pause("You choose not to fight and try to escape.")
    else:
        print_pause("Invalid input. Please enter 1 or 2.")
        return encounter_enemy(total_score)
    return total_score

def meet_stranger(total_score):
    print_pause("While exploring the forest, you come across a friendly stranger.")
    print_pause("The stranger offers you a valuable item.")
    print_pause("Do you accept? (1) Yes (2) No")
    choice = input()
    if choice == '1':
        item = random.choice(['Sword', 'Shield', 'Potion'])
        print_pause(f"You graciously accept the {item} from the stranger.")
        total_score += 3
    elif choice == '2':
        print_pause("You politely decline the stranger's offer.")
    else:
        print_pause("Invalid input. Please enter 1 or 2.")
        return meet_stranger(total_score)
    return total_score

def play_game():
    intro()
    total_score = 0
    while total_score >= 0:
        print_pause("You have three options:")
        print_pause("1. Explore the forest.")
        print_pause("2. Proceed cautiously to avoid enemies.")
        print_pause("3. Interact with a stranger.")
        choice = input("What would you like to do?\n")
        if choice == '1':
            total_score = explore_forest(total_score)
        elif choice == '2':
            total_score = encounter_enemy(total_score)
        elif choice == '3':
            total_score = meet_stranger(total_score)
        else:
            print_pause("Invalid input. Please enter 1, 2, or 3.")

        if total_score >= 20:
            print_pause("Congratulations! You have achieved a high score.")
            print_pause("You win!")
            break
        elif total_score <= -10:
            print_pause("Your score is too low. Game over!")
            break

    print_pause("Thank you for playing. Goodbye!")

play_game()