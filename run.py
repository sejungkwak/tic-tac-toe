# Game board
board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
def display_board(board):
  
  for slot in board:
    if slot in board[:2] or slot in board[3:5] or slot in board[6:8]:
      print(f" {slot} |", end="")
    if slot == 9 or slot == 6:
      print(f" {slot} ")
      print("-----------")
    if slot == 3:
      print(f" {slot} ")

# Displays the information
def dsiplay_greeting():
  print("Welcome to Tic Tac Toe!")
  display_board(board)
  game_setting()

# Player 1's chracter
def game_setting():
  
  player1 = 'A'
  choice = ['X', 'O']

  while player1.upper() not in choice:
    player1 = input("Player 1: Do you want to be X or O?")

    if player1.upper() in choice:
      break

    else:
      print("You have entered an invalid answer. "
        "Please enter X or O.")

  print(f"Player 1 is {player1.upper()}. "
    "Player 1 will go first.")
  player_ready()

# Ready to play
def player_ready():

  ready = 'A'
  choice = ['Y', 'N']

  while ready.upper() not in choice:
    ready = input("Are you ready to play? "
              "Please enter [Y]es or [N]o.")
    
    if ready.upper() in choice:
      break

    else:
      print("You have entered an invalid answer. "
        "Please enter Y or N.")

# Win conditions
def check_win(board):

  if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] ==board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
    print("Congratulations! You have won the game!")
    play_again()
  else:
    pass
    
# Play again
def play_again():
  answer = 'A'
  choice = ['Y', 'N']

  while answer.upper() not in choice:
    answer = input("Do you want to play again? "
      "Please enter [Y]es / [N]o")
    
    if answer.upper() == 'Y':
      board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
      dsiplay_greeting()
      break
    elif answer.upper() == 'N':
      print("Thank you for playing :)")
      break
    else:
      print("Please enter Y or N.")

# Gets user input

# Validates user input

# Updates game board

# Displays result