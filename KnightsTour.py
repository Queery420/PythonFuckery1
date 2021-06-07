# KnightsTour.py "Knight's Tour"
# Originally written by Ivy Slick (@Queery420) on 6/3/21
# A Knight's Tour is an algorithm in which the Chess Knight
# visits all squares of a square board with a side at least
# 5 squares long exactly once. This tour uses Depth-First
# Search.



def main():
    print('Please enter the side length: ', end='')
    BS = input()
    BoardSide = int(BS)
    Board = [[False]*BoardSide]*BoardSide
    knightVisits = [""]*(BoardSide ^ 2)
    numKnightVisits = (BoardSide ^ 2) - 1


    def checkBoard():
        for i in range(BoardSide):
            for j in range(BoardSide):
                if Board[i][j] == False:
                    return False
        return True


    def getKnightVisit(x, y):


        global knightVisits
        global numKnightVisits
        
        Board[x][y] = True
        
        # +2, +1
        if ((x + 2) < BoardSide) and ((y + 1) < BoardSide):
            if Board[(x + 2)][(y + 1)] == False:
                if getKnightVisit(x + 2, y + 1):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # +2, -1
        if ((x + 2) < BoardSide) and ((y - 1) >= 0):
            if Board[(x + 2)][(y - 1)] == False:
                if getKnightVisit(x + 2, y - 1):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # +1, +2
        if ((x + 1) < BoardSide) and ((y + 2) < BoardSide):
            if Board[(x + 1)][(y + 2)] == False:
                if getKnightVisit(x + 1, y + 2):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # +1, -2
        if ((x + 1) < BoardSide) and ((y - 2) >= 0):
            if Board[(x + 1)][(y - 2)] == False:
                if getKnightVisit(x + 1, y - 2):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -1, +2
        if ((x - 1) >= 0) and ((y + 2) < BoardSide):
            if Board[(x - 1)][(y + 2)] == False:
                if getKnightVisit(x - 1, y + 2):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -1, -2
        if ((x - 1) >= 0) and ((y - 2) >= 0):
            if Board[(x - 1)][(y - 2)] == False:
                if getKnightVisit(x - 1, y - 2):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -2, +1
        if ((x - 2) >= 0) and ((y + 1) < BoardSide):
            if Board[(x - 2)][(y + 1)] == False:
                if getKnightVisit(x - 2, y + 1):
                    #print (str(x) + ", " + str(y))
                    knightVisits[numKnightVisits] = str(x + 1) + ", " + str(y + 1)
                    numKnightVisits = numKnightVisits - 1
                    return True
        # -2, -1
        if ((x - 2) >= 0) and ((y - 1) >= 0):
            if Board[(x - 2)][(y - 1)] == False:
                if getKnightVisit(x - 2, y - 1):
                    #print (str(x) + ", " + str(y))
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

    print("Knight's Tour will now execute.")
    if getKnightVisit(0, 0):
        print("The Knight's Visits, in order:")
        for i in range(len(knightVisits)):
            print(knightVisits[i])
    else:
        print("It didn't work")

if __name__ == "__main__":
    main()
