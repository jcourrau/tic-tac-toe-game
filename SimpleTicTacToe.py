import random


# Create the board
board = [[ row*3 + col + 1 for col in range(3)] for row in range(3)]
choices= [5] # Initial Computer move
 

# Function to display the board
def show_board(board):
    print("+-------"*3+"+")
    
    for row in board:
        print("|       "*3+"|")
        print("".join(f"|   {cell}   " for cell in row) + "|")
        print("|       "*3+"|")
        print("+-------"*3+"+")

# Function to mark a position on the board
def board_mark(board,pos,mark = "X"):
    
    if pos < 1 or pos > 9:
        return False
    
    # Convert number to row and column index
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    
    if not isinstance(board[row][col], int):
        return False
          
    # Change the board
    board[row][col] = mark
    return True

# Function to check winning conditions
def check_win(board,mark):
    winner = "Player" if mark == "O" else "Computer"
    
    # Check Rows
    for row in board:
        if all(cell == mark for cell in row):
            return True, winner 
        
    # Check Columns
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True, winner 
    
    # Check diagonals
    # Left-to-right diagonal
    if all(board[i][i] == mark for i in range(3)):
        return True, winner 
    
    # Right-to-left diagonal
    if all(board[i][2 - i] == mark for i in range(3)):
        return True, winner 
    
    # If there are no posibilities left.
    if all(not isinstance(cell, int) for row in board for cell in row):
        return True, "Tie"
    
    return False, None  # No winner
        
# Function for the computer to make a move
def computer_play(board):
    
    while True:
        choice = random.randint(1, 9)
        if board_mark(board, choice, "X"):
            choices.append(choice)
            return choice
    

# Function for the player to make a mov
def player_play(board):
    
    while True:
        try:
            choice = int(input("Enter your move: "))
            
            if choice not in choices and board_mark(board,choice,"O"):
                choices.append(choice)
                break
            else:
                print("Invalid move or position already marked!")
                
        except ValueError:
            print("Please enter a valid number.")

# Start
board_mark(board,5,"X")
show_board(board)
print(f"The computer has played position 5")
player_play(board)

# Game Loop
win = False
while win == False:
    pos = computer_play(board)
    show_board(board)
    print(f"The computer has played position {pos}")
    win, winner = check_win(board,"X")
    if win:
        break
    
    player_play(board)
    win, winner = check_win(board,"O")
    
    
if winner == "Tie":
    print("Is a Tie!")
else:
    print(f"{winner} wins!")