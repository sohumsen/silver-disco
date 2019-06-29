# Game of life v1
#sohum sen

#DOESNT WORK
#some cells arent dying
#some cells arent living


#TODO
#make user type in staring positions
#make user type in number of generations
#make the program loop through multiple generation

# IWANTTO
# add machine learning somewhow


#make the board with generators 10*10
def makeboard(): 
  global board
  n = 10
  m = 10
  board = [["."] * m for i in range(n)]

#seeds of life initialise
def seeds():
  board[4][4]=0
  board[4][5]=0
  board[5][4]=0
  board[5][6]=0
  board[8][8]=0
  board[6][6]=0
  board[3][4]=0


#main checking of the board
def scanboard():
  for i in range(len(board)):
    for j in range(len(board)):

      #check if its safe to pass in i,j
      if i==len(board) or i ==(len(board)-1) or j==len(board) or j ==(len(board)-1):
        continue

      #i and j are alive, so test their surroundings
      if board[i][j] ==0:
        state= alivearound(i,j)
        board[i][j]=state

      #i and j are dead, so test their surroundings
      else:
        deatharound(i,j)


#how many cells are alive around i,j
def counter(i,j):
  count=0
  if board[i+1][j] == 0:
    count+=1
  if board[i+1][j-1] ==0:
    count+=1
  if board[i+1][j+1] ==0:
    count+=1
  if board[i-1][j] ==0:
    count+=1
  if board[i-1][j-1] ==0:
    count+=1
  if board[i-1][j+1] ==0:
    count+=1
  if board[i][j+1] ==0:
    count+=1
  if board[i][j-1] ==0:
    count+=1

  return count

#if the cell is alive, what are the next steps
def alivearound(i,j):
  count = counter(i,j)

  #it survives to the next genearation
  if count==2 or count==3:
    return 0
    #board[i][j]=0

  #it dies
  else:
    return "."
    #board[i][j]="."


#if the cell is dead, what are the next steps
def deatharound(i,j):
  count = counter(i,j)

  #a dead cell becomes alive
  if count==3:
    board[i][j]="0"
  
  # a dead cell stays dead,shocker
  else:
    pass
    


#print the board
def printboard():
  for row in board:
      print(' '.join([str(elem) for elem in row]))


#everything in the main function
def main():
  makeboard()
  seeds()
  for i in range(4):
    scanboard()
    print("\n")
    printboard()


main()
