import time
import random

# Function to add a pause between printing messages
def print_pause(message):
    print(message)
    time.sleep(0.5)

# Function to introduce the game and set the mission
def intro():
    print_pause("Welcome to the Adventure Game!")
    print_pause("You find yourself in a mysterious forest.")
    print_pause("Your mission is to find the hidden treasure.")
    print_pause("Be careful, danger lurks in every corner.")


def print_score(total_score):
    print_pause(f"Your current score is: {total_score}")

# Function to explore the forest and encounter different scenarios
def explore_forest(total_score):
    print_pause("You start exploring the forest.")
    print_pause("As you walk, you hear strange sounds and see peculiar creatures.")
    
    # Randomly choose one of three main scenarios
    main_scenario = random.choice([1, 2, 3])
    
    if main_scenario == 1:
        print_pause("While wandering through the forest, you stumble upon a hidden treasure chest.")
        print_pause("Do you want to open the chest? (1) Yes (2) No")
        choice = input()
        if choice == '1':
            # Randomly determine the outcome of opening the chest
            outcome = random.choice([1, 2, 3])
            if outcome == 1:
                print_pause("You open the chest and find a stash of gold coins!")
                print_pause("Congratulations! You have found treasure. Your score increases!")
                total_score += 10
            elif outcome == 2:
                print_pause("As you open the chest, a cloud of poisonous gas emerges.")
                print_pause("You quickly retreat, avoiding the danger.")
                print_pause("Your score remains unchanged.")
            else:
                print_pause("Upon opening the chest, a mischievous forest spirit appears.")
                print_pause("The spirit grants you a small magical trinket.")
                print_pause("Your score slightly increases.")
                total_score += 3
        elif choice == '2':
            print_pause("You decide not to open the chest and continue exploring.")
        else:
            print_pause("Invalid input. Please enter 1 or 2.")
            return explore_forest(total_score)
    
    elif main_scenario == 2:
        print_pause("While exploring the forest, you come across a hidden waterfall.")
        print_pause("Do you want to take a closer look? (1) Yes (2) No")
        choice = input()
        if choice == '1':
            outcome = random.choice([1, 2, 3])
            if outcome == 1:
                print_pause("As you approach the waterfall, you discover a hidden cave behind it.")
                print_pause("Inside the cave, you find ancient artifacts.")
                print_pause("Your score increases as you uncover valuable relics.")
                total_score += 8
            elif outcome == 2:
                print_pause("You step closer to the waterfall and slip on a wet rock.")
                print_pause("You fall into the water but manage to swim back to safety.")
                print_pause("Your score remains unchanged.")
            else:
                print_pause("You admire the beauty of the waterfall and feel refreshed.")
                print_pause("The serene atmosphere increases your energy.")
                print_pause("Your score slightly increases.")
                total_score += 3
        elif choice == '2':
            print_pause("You decide not to explore the waterfall and continue your journey.")
        else:
            print_pause("Invalid input. Please enter 1 or 2.")
            return explore_forest(total_score)
    
    else:
        print_pause("As you walk deeper into the forest, you notice a peculiar stone circle.")
        print_pause("Do you want to investigate? (1) Yes (2) No")
        choice = input()
        if choice == '1':
            outcome = random.choice([1, 2, 3])
            if outcome == 1:
                print_pause("You examine the stone circle and discover hidden markings.")
                print_pause("Deciphering the markings reveals a secret map.")
                print_pause("Your score increases as you gain valuable knowledge.")
                total_score += 5
            elif outcome == 2:
                print_pause("As you approach the stone circle, a swarm of bees emerges.")
                print_pause("You quickly retreat to avoid their stings.")
                print_pause("Your score remains unchanged.")
            else:
                print_pause("You sit in the middle of the stone circle and meditate.")
                print_pause("The tranquil atmosphere replenishes your spirit.")
                print_pause("Your score slightly increases.")
                total_score += 2
        elif choice == '2':
            print_pause("You decide not to investigate the stone circle and continue your journey.")
        else:
            print_pause("Invalid input. Please enter 1 or 2.")
            return explore_forest(total_score)
    print_score(total_score)
    return total_score

# Function to encounter an enemy and engage in a duel
def encounter_enemy(total_score):
    print_pause("As you venture deeper into the forest, you encounter a fearsome enemy.")
    print_pause("The enemy challenges you to a duel.")
    print_pause("Do you want to fight? (1) Yes (2) No")
    choice = input()
    if choice == '1':
        # Randomly determine the outcome of the battle
        outcome = random.choice([1, 2, 3, 4, 5, 6])
        if outcome == 1:
            print_pause("You summon all your courage and engage in a fierce battle.")
            print_pause("With your exceptional skills, you defeat the enemy!")
            total_score += 5
        elif outcome == 2:
            print_pause("The enemy proves to be too strong for you.")
            print_pause("You barely escape with your life intact.")
            total_score -= 3
        elif outcome == 3:
            print_pause("You manage to land a few good hits on the enemy.")
            print_pause("Injured, the enemy retreats, allowing you to continue your journey.")
            total_score += 2
        elif outcome == 4:
            print_pause("You find a hidden shortcut during the battle.")
            print_pause("You make a swift escape, leaving the enemy behind.")
            total_score += 3
        elif outcome == 5:
            print_pause("You cleverly trick the enemy, gaining the upper hand in the fight.")
            print_pause("Confused, the enemy surrenders and flees the scene.")
            total_score += 4
        else:
            print_pause("You engage in an epic battle but end up in a stalemate.")
            print_pause("Both you and the enemy retreat, preparing for future encounters.")
            total_score += 1
    elif choice == '2':
        print_pause("You choose not to fight and try to escape.")
    else:
        print_pause("Invalid input. Please enter 1 or 2.")
        return encounter_enemy(total_score)
    print_score(total_score)
    return total_score

# Function to meet a stranger and interact with them
def meet_stranger(total_score):
    print_pause("While exploring the forest, you come across a friendly stranger.")
    print_pause("The stranger offers you a valuable item.")
    print_pause("Do you accept? (1) Yes (2) No")
    choice = input()
    if choice == '1':
        # Randomly determine the outcome of accepting the item
        outcome = random.choice([1, 2, 3, 4, 5, 6])
        if outcome == 1:
            item = 'Sword'
            print_pause(f"You graciously accept the {item} from the stranger.")
            total_score += 3
        elif outcome == 2:
            item = 'Shield'
            print_pause(f"You graciously accept the {item} from the stranger.")
            total_score += 3
        elif outcome == 3:
            item = 'Potion'
            print_pause(f"You graciously accept the {item} from the stranger.")
            total_score += 3
        elif outcome == 4:
            print_pause("The stranger gives you an old map with hidden treasures marked.")
            print_pause("You gain valuable information.")
            total_score += 5
        elif outcome == 5:
            print_pause("The stranger challenges you to a friendly game of riddles.")
            print_pause("If you answer correctly, you'll be rewarded.")
            answer = input("What has a heart that doesn't beat? ")
            if answer.lower() == "artichoke":
                print_pause("Congratulations! You answered correctly.")
                print_pause("The stranger rewards you with a rare artifact.")
                total_score += 7
            else:
                print_pause("Oops! That's incorrect.")
                print_pause("The stranger leaves disappointed, and you gain no score.")
        else:
            print_pause("The stranger turns out to be a disguised enemy!")
            print_pause("You engage in a battle to defend yourself.")
            # Randomly determine the outcome of the battle with the disguised enemy
            outcome = random.choice(['win', 'lose'])
            if outcome == 'win':
                print_pause("You defeat the enemy and continue your journey.")
                total_score += 5
            else:
                print_pause("The enemy overwhelms you. You lose the battle.")
                print_pause("Game over!")
                total_score -= 5
    elif choice == '2':
        print_pause("You politely decline the stranger's offer.")
    else:
        print_pause("Invalid input. Please enter 1 or 2.")
        return meet_stranger(total_score)
    print_score(total_score)
    return total_score

# Function to start the game and handle the main gameplay loop
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

        if total_score >= 10:
            win_sentences = [
                "Congratulations! You have achieved a high score.",
                "You have conquered the forest and found the ultimate treasure!",
                "With bravery and wit, you emerge victorious!",
                "You are a true adventurer! Well done!",
                "The forest bows down to your greatness."
                ]
            print_pause(random.choice(win_sentences))
            print_pause("You win!")
            print_pause("\nDo you want to play again? (1) Yes (2) No")
            choice = input()
            if choice == "1":
                play_game()
            else:
                break

        elif total_score <= -5:
            lose_sentences = [
                "Your score is too low. Game over!",
                "Defeat engulfs you. The forest claims another victim.",
                "You couldn't withstand the perils of the forest. Game over!",
                "Your journey ends here. Better luck next time.",
                "The forest swallows you whole."
                ]
            print_score(total_score)
            print_pause(random.choice(lose_sentences))
            print_pause("\nDo you want to play again? (1) Yes (2) No")
            choice = input()
            if choice == "1":
                play_game()
            else:
                break

            

# Start the game
play_game()
