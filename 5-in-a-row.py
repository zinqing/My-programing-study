class chessboard:
    # use 0 for blank, 1 for black, 2 for white

    board = [ ]
    current = 2
    winner = 0
    role = {'0': 'blank','1': 'black','2': 'white'}

    def clear(self):
        self.board = [ ]
        self.current = 2
        self.winner = 0

    def creat(self):
        for x in range(14):
            self.board.append([ ])
            for y in range(14):
                self.board[ x ].append([ 0 ])

    def check(self,x,y,countmax=0):
        # return true if current is winner, else false

        dirs = [ [ 1,0 ],[ 1,1 ],[ 0,1 ],[ 1,-1 ] ]
        self.current = self.board[ x ][ y ]
        for coefficient in dirs:
            i,j = coefficient
            countcurrent = 0
            for k in range(-4,5):
                if self.current == self.board[ x + i * k ][ y + j * k ]:
                    countcurrent += 1
                else:
                    countcurrent = 0
                if countcurrent > countmax:
                    countmax = countcurrent

        return countmax == 5

    def black(self,x,y):
        # return 1 if it is able to put chess, else return 0
        # print(x,y)
        # print(self.board[ x ][ y ])
        if (x <= 14) and (y <= 14) and (self.board[ x ][ y ] == [ 0 ]):
            self.board[ x ][ y ] = 1
            self.current = 1
            return 1
        else:
            print('error')
            return 0

    def white(self,x,y):
        if (x <= 14) and (y <= 14) and (self.board[ x ][ y ] == [ 0 ]):
            self.board[ x ][ y ] = 2
            self.current = 2
            return 1
        else:
            return 0


board = chessboard()
board.clear()
board.creat()
# print(board.board[ 5 ][ 5 ])

while 1:

    cammand = input("what is your move? ")
    # print(cammand.split(',')[ 0 ])
    x = int(cammand.split(',')[ 0 ])
    y = int(cammand.split(',')[ -1 ])
    # print(x,y)

    if board.current == 2:
        if board.black(x,y):

            if board.check(x,y):
                board.winner = board.current
                break
            else:
                pass
        else:
            print('you can not move here!')
            board.current = 2
    else:
        if board.white(x,y):
            if board.check(x,y):
                board.winner = board.current
                break
            else:
                pass
        else:
            print('you can not move here!')
            board.current = 1
print(board.role[ str(board.winner) ] + "is the winner!")
