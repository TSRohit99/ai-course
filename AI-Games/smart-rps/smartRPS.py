import random

# Track how often the human plays each move
human_counts = {'rock': 0, 'paper': 0, 'scissors': 0}

# What beats what
beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def get_human_choice():
    choice = input("Enter rock, paper or scissors: ").strip().lower()
    if choice not in human_counts:
        print("Invalid input! Please enter rock, paper, scissors.")
        return get_human_choice()
    return choice

def get_ai_choice():
    total = sum(human_counts.values())
    # For the first few rounds, pick randomly
    if total <= 3:
        ai = random.choice(list(human_counts))
        reason = "used random choice because not enough data yet"
        chance = None
    else:
        # find human's most frequent play, and pick the move that beats it
        most_common = max(human_counts, key=human_counts.get)
        ai = beats[beats[most_common]]  # AI picks what beats the human's most common move
        chance = human_counts[most_common] / total * 100
        reason = f"you played {most_common} {human_counts[most_common]} out of {total} times"
    
    # Print explanation
    if chance is None:
        print(f"AI chose {ai} ({reason}).")
    else:
        print(f"AI chose {ai} because {reason} ({chance:.1f}% chance).")
    return ai

def decide_winner(human, ai):
    if human == ai:
        return "Tie!"
    # Human wins if their move beats AI's move
    return "You win!" if beats[human] == ai else "AI wins!"

def main():
    rounds = int(input("How many rounds? "))
    human_wins = 0
    ai_wins = 0
    ties = 0
    
    for round_num in range(1, rounds+1):
        print(f"\nRound {round_num}")
        human = get_human_choice()
        
        # Record human's play before AI makes its choice
        human_counts[human] += 1
        
        ai = get_ai_choice()
        
        print(f"You chose: {human}")
        result = decide_winner(human, ai)
        print(result)
        
        # Track score
        if result == "You win!":
            human_wins += 1
        elif result == "AI wins!":
            ai_wins += 1
        else:
            ties += 1
    
    print("\nFinal stats (your move frequencies):")
    for move, cnt in human_counts.items():
        print(f"  {move.capitalize()}: {cnt}")
    
    print(f"\nFinal score - You: {human_wins}, AI: {ai_wins}, Ties: {ties}")

if __name__ == "__main__":
    main()