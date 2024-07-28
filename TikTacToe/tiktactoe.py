import random

# Function to update the Matrix, also handling the errors of selecting the same location again or choosing the wrong location
def tiktok(player, is_automated=False):
    if is_automated:
        # Automated player makes a move
        while True:
            i, j = random.randint(0, 2), random.randint(0, 2)
            if arr[i][j] is None:
                arr[i][j] = player
                break
    else:
        # Human player makes a move
        while True:
            try:
                print(f"Enter the row and column for player {player} (row col): ", end="")
                i, j = map(int, input().split())
                if i > 2 or i < 0 or j > 2 or j < 0:
                    print("You are getting out of range, Buddy")
                elif arr[i][j] is not None:
                    print("This has been occupied. Choose another one please.")
                else:
                    arr[i][j] = player
                    break
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

# Check for winner
def conditions():
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] != None:
            return arr[i][0]
    for j in range(3):
        if arr[0][j] == arr[1][j] == arr[2][j] != None:
            return arr[0][j]
    if arr[0][0] == arr[1][1] == arr[2][2] != None:
        return arr[0][0]
    if arr[0][2] == arr[1][1] == arr[2][0] != None:
        return arr[0][2]
    return None

# Displaying the Matrix
def display():
    for row in arr:
        print(row)
    print()

# Game loop for Human vs. Human
def human_vs_human():
    global arr
    arr = [[None, None, None] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0
    count = 0
    
    while True:
        count += 1
        if count > 9:
            print("IT'S A DRAW")
            break
        
        # Make a move for the current player
        tiktok(players[current_player_index])
        display()
        
        # Check for winner
        winner = conditions()
        if winner:
            print(f"PLAYER {players.index(winner) + 1} ({winner}) WON")
            break
        
        # Switch players
        current_player_index = 1 - current_player_index

# Game loop for Human vs. Computer
def human_vs_computer():
    global arr
    arr = [[None, None, None] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0
    count = 0
    automated_player_index = 1  # Assuming player "O" is automated; change to 0 if "X" is automated
    
    while True:
        count += 1
        if count > 9:
            print("IT'S A DRAW")
            break
        
        # Determine if the current player is automated
        is_automated = (current_player_index == automated_player_index)
        
        # Make a move for the current player
        tiktok(players[current_player_index], is_automated)
        display()
        
        # Check for winner
        winner = conditions()
        if winner:
            print(f"PLAYER {players.index(winner) + 1} ({winner}) WON")
            break
        
        # Switch players
        current_player_index = 1 - current_player_index

# Main function to choose game mode and play
def main():
    while True:
        print("Choose game mode:")
        print("1. Human vs. Human")
        print("2. Human vs. Computer")
        mode = input("Enter the number of your choice: ")
        
        if mode == "1":
            human_vs_human()
        elif mode == "2":
            human_vs_computer()
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        
        again = input("Do you want to play again (Y/N)? ")
        if again.lower() != "y":
            break

# Run the main function
if __name__ == "__main__":
    main()