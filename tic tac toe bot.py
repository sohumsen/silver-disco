#TIC TAC TOE AI GAME#--COMPLETED
#v1 Sohum Sen
import sys
import random
#ALL COMMENTS
  #ai doesnt run block or win moves-DONE
  #Player can overwrite moves-DONE
  #check for winners-DONE
  #randomize the corner moves-NO NEED
  #change the order of players-DONE

#make the board with generators 10*10
def make_board(): 
  global board
  n = 3
  m = 3
  board = [["."] * m for i in range(n)]
  print_board()

def print_board():
  for row in board:
    print('  '.join([str(elem) for elem in row]))
  print(" ")

def get_players():
  choice_valid=False
  while choice_valid==False:

    player_piece=input("Do you want to be X or O ? ")
    if player_piece=="X" or player_piece=="O":

      choice_valid=True


  return player_piece

def player_make_move(player_piece):
  choice_valid=False

  while choice_valid==False:


    player_move = int(input("Enter the move between 1-9 numpad layout: "))
    if len(str(player_move))==1 and (player_move)<=9:
      choice_valid=True

  move_convert(player_move,player_piece)
  
def move_convert(player_move,player_piece):

  i=[]
  if player_move ==1:
    i=[2,0] 
  if player_move ==2:
    i=[2,1] 
  if player_move ==3:
    i=[2,2] 
  if player_move ==4:
    i=[1,0] 
  if player_move ==5:
    i=[1,1] 
  if player_move ==6:
    i=[1,2] 
  if player_move ==7:
    i=[0,0] 
  if player_move ==8:
    i=[0,1] 
  if player_move ==9:
    i=[0,2] 

  if board[int(i[0])][int(i[1])] == ".":

    board[int(i[0])][int(i[1])] = player_piece
    print_board()
  
  else:

    player_make_move(player_piece)

def think_of_move(player_piece):
  
  if player_piece=="X":
    bot_piece="O"
  else:
    bot_piece="X"

  win_combos= ["000102","101112","202122","001020","011121","021222","001122","021120"]

  ai_move=[]

  def win():
    ai_move=[]
    for i in range(0,8):
      
      if board[int(win_combos[i][0])][int(win_combos[i][1])]== bot_piece and board[int(win_combos[i][2])][int(win_combos[i][3])]==bot_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==".":


        ai_move=[(int(win_combos[i][4])), (int(win_combos[i][5])) ]

     
      elif board[int(win_combos[i][0])][int(win_combos[i][1])]== bot_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==bot_piece and board[int(win_combos[i][2])][int(win_combos[i][3])]==".":


        ai_move=[(int(win_combos[i][2])), (int(win_combos[i][3])) ]


      elif board[int(win_combos[i][2])][int(win_combos[i][3])]== bot_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==bot_piece and board[int(win_combos[i][0])][int(win_combos[i][1])]==".":



        ai_move=[(int(win_combos[i][0])), (int(win_combos[i][1]))]

    return ai_move

  def block():
    ai_move=[]
    for i in range(0,8):
      #101112
      if board[int(win_combos[i][0])][int(win_combos[i][1])]== player_piece and board[int(win_combos[i][2])][int(win_combos[i][3])]==player_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==".":

        ai_move=[(int(win_combos[i][4])), (int(win_combos[i][5])) ]

      elif board[int(win_combos[i][0])][int(win_combos[i][1])]== player_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==player_piece and board[int(win_combos[i][2])][int(win_combos[i][3])]==".":

        ai_move=[(int(win_combos[i][2])), (int(win_combos[i][3])) ]

      elif board[int(win_combos[i][2])][int(win_combos[i][3])]== player_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==player_piece and board[int(win_combos[i][0])][int(win_combos[i][1])]==".":

        ai_move=[(int(win_combos[i][0])), (int(win_combos[i][1])) ]

    return ai_move

  def center():
    ai_move=[]
    if board[1][1]==".":
    #  board[1][1]=bot_piece
      ai_move=[1,1]


    return ai_move
    
  def empty_corner():
    ai_move=[]
    x=random.randint(0,3)
    if board[0][0]==".":

      ai_move=[0,0]     

    elif board[2][0]==".":
      ai_move=[2,0]

    elif board[0][2]==".":
      ai_move=[0,2]

    elif board[2][2]==".":
      ai_move=[2,2]

    return ai_move

  def empty_side():
    ai_move=[]
    if board[0][1]==".":
      ai_move=[0,1]

    elif board[1][0]==".":
      ai_move=[1,0]
      

    elif board[1][2]==".":
      ai_move=[1,2]
      

    elif board[2][1]==".":
      ai_move=[2,1]


      
    return ai_move
#ai_move contains 2 numbers for the coordinates
  if len(win())!=0:
    board[win()[0]][win()[1]]=bot_piece
  elif len(block())!=0:
    board[block()[0]][block()[1]]=bot_piece
  elif len(center())!=0:
    board[center()[0]][center()[1]]=bot_piece
  elif len(empty_corner())!=0:
    board[empty_corner()[0]][empty_corner()[1]]=bot_piece
  elif len(empty_side())!=0:
    board[empty_side()[0]][empty_side()[1]]=bot_piece
  print_board()

def check_for_winner(player_piece):
  if player_piece=="X":
    bot_piece="O"
  else:
    bot_piece="X"

  win_combos= ["000102","101112","202122","001020","011121","021222","001122","021120"]
  winner=" "

  for i in range(0,8):
    if board[int(win_combos[i][0])][int(win_combos[i][1])]== bot_piece and board[int(win_combos[i][2])][int(win_combos[i][3])]==bot_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==bot_piece:
      winner="bot"

    elif board[int(win_combos[i][0])][int(win_combos[i][1])]== player_piece and board[int(win_combos[i][2])][int(win_combos[i][3])]==player_piece and board[int(win_combos[i][4])][int(win_combos[i][5])]==player_piece:
      winner="player"

  if winner=="player":
    print("player WINS")
    sys.exit()
    
  elif winner=="bot":
    print("bot WINS,loser")
    sys.exit()
        
def main():
  print("Tic Tac Toe AI game\n")
  make_board()
  player_piece= get_players()
  if player_piece=="X":
    print("PLAYER move:")
    player_make_move(player_piece)
    while True:

      print("BOT move:")
      think_of_move(player_piece)

      check_for_winner(player_piece)

      print("PLAYER move:")
      player_make_move(player_piece) 

      check_for_winner(player_piece)

      if not any("." in x for x in board):
        print("Draw-End")
        sys.exit()
        break
  else:
    print("BOT move:")
    think_of_move(player_piece)
    while True:

      print("PLAYER move:")
      player_make_move(player_piece) 

      check_for_winner(player_piece)

      print("BOT move:")
      think_of_move(player_piece)

      check_for_winner(player_piece)
      
      if not any("." in x for x in board):
        print("Draw-End")
        sys.exit()
        break

main()






























