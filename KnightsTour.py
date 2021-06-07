# KnightsTour.py "Knight's Tour"
# Originally written by Ivy Slick (@Queery420) on 6/3/21
# I got help with this code on r/LearnPython, thread for code attribution:
# https://www.reddit.com/r/learnpython/comments/nuc2pn/variable_scope_and_2d_arrays/
#
# A Knight's Tour is an algorithm in which the Chess Knight
# visits all squares of a square board with a side at least
# 5 squares long exactly once. This tour is an "Open Tour",
# or one which starts and ends on different squares, as
# opposed to a "Closed Tour" which would end on the square
# where it began. This tour demonstrates Depth-First Search.



def main():
    # get the size of the board from the user. the board will be size BS * BS
    print('Please enter the side length: ', end='')
    BS = input()
    BoardSide = int(BS)

    # initialize the board to all False statements.
    # This code was suggested by several redditors in the aforementioned thread
    Board = [[False for _ in range(BoardSide)] for _ in range(BoardSide)]
    knightVisits = [""]*(BoardSide ** 2)
    numKnightVisits = (BoardSide ** 2) - 1



    # checkBoard simply checks to see if the board is full of True statements
    # returns false when it encounters any False value in the board, and
    # returns true when no False values are encountered
    # checkBoard is relatively inefficient, as each check takes exponentially
    # more time to process as the board size increases.
    def checkBoard():
        for i in range(BoardSide):
            for j in range(BoardSide):
                if Board[i][j] == False:
                    return False
        return True
    #end checkBoard



    # getKnightVisit is a recursive statement, and is the Depth-First Search.
    # This function first sets the "visited" square to True, to mark that the
    # square has been visited in the search. It then checks to see if square
    # x + 2, y + 1 is not outside the board, then checks that that square has
    # not yet been visited (the square is False). If the square is valid and
    # unvisited, the algorithm calls a new instance of itself on that square.
    # When the search reaches a position from which it can make no more moves
    # (reaches a potential end-state), it checks the board for any unvisited
    # squares, and returns True if none are found and False if any are found.
    # If it returns false, it also sets the square back to False.
    # If an instance of the function returns True, it will cause all active
    # instances of the function to iteratively return True as well from its
    # solved state (checkBoard() returns True) to the initial call from main().
    # Lastly, as it is cascading back it sets a list each square a string array.
    def getKnightVisit(x, y):

        nonlocal numKnightVisits
        nonlocal knightVisits
        nonlocal Board

        Board[x][y] = True

        # +2, +1
        if ((x + 2) < BoardSide) and ((y + 1) < BoardSide):
            if Board[(x + 2)][(y + 1)] == False:
                if getKnightVisit(x + 2, y + 1):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # +2, -1
        if ((x + 2) < BoardSide) and ((y - 1) >= 0):
            if Board[(x + 2)][(y - 1)] == False:
                if getKnightVisit(x + 2, y - 1):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # +1, +2
        if ((x + 1) < BoardSide) and ((y + 2) < BoardSide):
            if Board[(x + 1)][(y + 2)] == False:
                if getKnightVisit(x + 1, y + 2):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # +1, -2
        if ((x + 1) < BoardSide) and ((y - 2) >= 0):
            if Board[(x + 1)][(y - 2)] == False:
                if getKnightVisit(x + 1, y - 2):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -1, +2
        if ((x - 1) >= 0) and ((y + 2) < BoardSide):
            if Board[(x - 1)][(y + 2)] == False:
                if getKnightVisit(x - 1, y + 2):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -1, -2
        if ((x - 1) >= 0) and ((y - 2) >= 0):
            if Board[(x - 1)][(y - 2)] == False:
                if getKnightVisit(x - 1, y - 2):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -2, +1
        if ((x - 2) >= 0) and ((y + 1) < BoardSide):
            if Board[(x - 2)][(y + 1)] == False:
                if getKnightVisit(x - 2, y + 1):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -2, -1
        if ((x - 2) >= 0) and ((y - 1) >= 0):
            if Board[(x - 2)][(y - 1)] == False:
                if getKnightVisit(x - 2, y - 1):
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True

        if checkBoard():
            knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
            numKnightVisits = numKnightVisits - 1
            return True
        else:
            Board[x][y] = False
            return False
    #end getKnightVisit



    print("Knight's Tour will now execute.")
    # The current version starts at 0, 0 by default, but any numbers can be
    # entered. A future version may get input values for the initial position,
    # as the algorithm is capable of solving from any position.
    if getKnightVisit(0, 0):
        print("The Knight's Visits, in order:")
        for i in range(len(knightVisits)):
            print(str(i + 1) + ": " + knightVisits[i])
    else:
        print("It didn't work")
#end main



if __name__ == "__main__":
    main()
