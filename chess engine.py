##Chess Engine##
########################################################


black_king=u"\u2654"

black_queen=u"\u2655"

black_rook=u"\u2656"

black_bishop=u"\u2657"

black_knight=u"\u2658"

black_pawn=u"\u2659"

white_king=u"\u265A"

white_queen=u"\u265B"

white_rook=u"\u265C"

white_bishop=u"\u265D"

white_knight=u"\u265E"

white_pawn=u"\u265F"

def make_board():

  spaces=[" ", " ", " ", " ", " "," "," ", " "]
  board=[[black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook], [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],spaces,spaces,spaces,spaces, [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn], [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook]]
  

 

  for row in board:
    print(' | '.join([str(elem) for elem in row]))



# if we visualise the chess board as a 8*8 matrix, where it is positioned in the positive quadrant of a cartesian plane

#let the position of a piece be a cartesian coordinate, stored as a tuple e.g. [i,j] for x and y


#8|
#7|p  p  p  p  p  p  p  p
#6|
#5|
#4|
#3|
#2|p  p  p  p  p  p  p  p 
#1|r  h  b  q  k  b  h  r
#  [1][2][3][4][5][6][7][8]

def rules():
  def pawn_moves(pawn_position):

    new_pawn_position=[]
    if int(pawn_position[0]) ==" " and int(pawn_position[1])+1==" ":
      #pawn can be moved 1 step forward
      new_pawn_position= [pawn_position[0], (pawn_position[1]+1)]

      return new_pawn_position
    # TODO: check the moves history if its the first move because then it can move up to 2 spaces

  def bishop_moves(bishop_position):
    pass
  
  def knight_moves():
    pass

  def rook_moves():
    pass

  def king_moves():
    pass

  def queen_moves():
    pass




make_board()
rules()