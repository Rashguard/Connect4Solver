from __future__ import print_function
import sys

########################################################################
#Methods
class game(object):
    def __init__(self):
        self.possibleMove = []
        self.board = []
        self.numRow = 6
        self.numCol = 7

    def printBoard(self, board):
        print()

        print(' ', end='')
        for x in range(1, self.numCol + 1):
            print(' %s  ' % x, end='')
        print()

        print('+---+' + ('---+' * (self.numCol - 1)))

        for y in range(self.numRow):
            print('|   |' + ('   |' * (self.numCol - 1)))
            print('|', end='')

            for x in range(self.numCol):
                print(' %s |' % self.board[x][y], end='')
            print()

            print('|   |' + ('   |' * (self.numCol - 1)))
            print('+---+' + ('---+' * (self.numCol - 1)))


    def resetBoard(self):
        board = []
        for x in range(self.numCol):
            board.append([" "] * self.numRow)
        self.board = board


    def makeMyMove(self, column):
        for y in range(self.numRow - 1, -1, -1):
            if self.board[column][y] == ' ':
                self.board[column][y] = 'O'
                return

    def makeEnemyMove(self, column):
        for y in range(self.numRow - 1, -1, -1):
            if self.board[column][y] == ' ':
                self.board[column][y] = 'X'
                return

    def checkWin(self, tile):
        # check horizontal spaces
        for y in range(self.numRow):
            for x in range(self.numCol - 3):
                if self.board[x][y] == tile and self.board[x+1][y] == tile and self.board[x+2][y] == tile and self.board[x+3][y] == tile:
                    return True

        # check vertical spaces
        for x in range(self.numCol):
            for y in range(self.numRow - 3):
                if self.board[x][y] == tile and self.board[x][y+1] == tile and self.board[x][y+2] == tile and self.board[x][y+3] == tile:
                    return True

        # check / diagonal spaces
        for x in range(self.numCol - 3):
            for y in range(3, self.numRow):
                if self.board[x][y] == tile and self.board[x+1][y-1] == tile and self.board[x+2][y-2] == tile and self.board[x+3][y-3] == tile:
                    return True

        # check \ diagonal spaces
        for x in range(self.numCol - 3):
            for y in range(self.numRow - 3):
                if self.board[x][y] == tile and self.board[x+1][y+1] == tile and self.board[x+2][y+2] == tile and self.board[x+3][y+3] == tile:
                    return True

        return False

    def solveAlg(self):
        return

    def solveRule(self):
        return




########################################################################
#Main
    
def main():

    while True:
        print("")
        print("CONNECT 4 SOLVER (6 x 7)")
        print("0. Reset Game")
        print("1. Solve using Search Algorithm")
        print("2. Solve using Rules")
        print("3. Input Enemy Move")
        print("4. Input My Move")
        print("9. Quit")
        sel = input("Select Menu: ")
        
        if sel ==9:
            print("")
            print("Exiting...")
            sys.exit()
            
        elif sel == 0:
            print("")
            print("Initializing...")

            currentGame = game()

            #Reset Game
            currentGame.resetBoard()
            gameBoard = currentGame.board
            currentGame.printBoard(gameBoard)
            
            print("===== R E S U L T S =====")
            print("Possible moves: ", end = "")

        elif sel == 1:

            # Do Something

            print("")
            print("===== R E S U L T S =====")
            
        
        elif sel == 2:
            
            # Do Something

            print("")
            print("===== R E S U L T S =====")
        
        elif sel == 3:

            enemyColumn = input("What column did the enemy choose:")
            move = enemyColumn - 1
            currentGame.makeEnemyMove(move)
            currentGame.printBoard(gameBoard)

            if currentGame.checkWin('X'):
                print("Enemy Wins!")


        elif sel == 4:

            myColumn = input("What column did you choose:")
            move = myColumn - 1
            currentGame.makeMyMove(move)
            currentGame.printBoard(gameBoard)

            if currentGame.checkWin('O'):
                print("You Win!")

        
            
########################################################################
if __name__ == '__main__':
    main()
