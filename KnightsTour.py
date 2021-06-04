# KnightsTour.py "Knight's Tour"
# Originally written by Ivy Slick (@Queery420) on 6/3/21
# A Knight's Tour is an algorithm in which the Chess Knight
# visits all squares of a square board with a side at least
# 4 square long exactly once. This tour uses Depth-First
# Search.


Finished = False

print('Please enter the side length: ', end='')
BoardSide = input()

numKnightVisits = BoardSide ^ 2
for i in range(BoardSide)
    for j in range(BoardSide)
        Board[i][j] = False

print("Knight's Tour will now execute.")

def knightVisit(x, y):
    if Board[x][y]
        toReturn = False
    else
        Board[x][y] = True
        numKnightVisits--
        toReturn = True
    return toReturn

def getKnightVisit(x, y):
    # +2, +1
    if ((x + 2) < BoardSide) && ((y + 1) < BoardSide)
        if knightVisit(x + 2, y + 1)
            getKnightVisit(x + 2, y + 1)
            if numKnightVisits == 0
                break
    # +2, -1
    if ((x + 2) < BoardSide) && ((y - 1) >= 0)
        if knightVisit(x + 2, y - 1)
            getKnightVisit(x + 2, y - 1)
            if numKnightVisits == 0
                break
    # +1, +2
    if ((x + 1) < BoardSide) && ((y + 2) < BoardSide)
        if knightVisit(x + 1, y + 2)
            getKnightVisit(x + 1, y + 2)
            if numKnightVisits == 0
                break
    # +1, -2
    if ((x + 1) < BoardSide) && ((y - 2) >= 0)
        if knightVisit(x + 1, y - 2)
            getKnightVisit(x + 1, y - 2)
            if numKnightVisits == 0
                break
    # -1, +2
    if ((x - 1) >= 0) && ((y + 2) < BoardSide)
        if knightVisit(x - 1, y + 2)
            getKnightVisit(x - 1, y + 2)
            if numKnightVisits == 0
                break
    # -1, -2
    if ((x - 1) >= 0) && ((y - 2) >= 0)
        if knightVisit(x - 1, y - 2)
            getKnightVisit(x - 1, y - 2)
            if numKnightVisits == 0
                break
    # -2, +1
    if ((x - 2) >= 0) && ((y + 1) < BoardSide)
        if knightVisit(x - 2, y + 1)
            getKnightVisit(x - 2, y + 1)
            if numKnightVisits == 0
                break
    # -2, -1
    if ((x - 2) >= 0) && ((y - 1) >= 0)
        if knightVisit(x - 2, y - 1)
            getKnightVisit(x - 2, y - 1)
            if numKnightVisits == 0
                break


getKnightVisit(0, 0)
