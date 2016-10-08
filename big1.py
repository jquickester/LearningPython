'''
print "A        B        C   "
print "1    X  | X  ","| X   "
print "_______________"
print "2       |   ","|    "
print "_______________"
print "3       |   ","|    "


game starts by saying
hello first player will be O's.
Please pick your places using the Grid 1-3 and A-C for example  1B, 3C


starts with empty list.
make list with X's moves
make list with O's moves

for each item in the X, and O lists put it on the board.


Winning  condition:
stop when  either X or O in
A1, A2, A3 OR
B1, B2, B3
C1, C2, C3

A1 B1 C1
A2  B2  C2
A3  B3  C3

A1  B2  C3
A3  B2  C1



stop when board is full = 9 turns taken

each time player picks a space board reprints itself
then goes to next player .

can't pick a space already picked.

'''
board = []
oinput = ['o']
xinput = ['x']


for i in range(1, 10):
    xinput = raw_input("x's take your turn")
    board.insert(0, xinput)
    oinput = raw_input("o take your turn")
    board.insert(0, oinput)

    print xinput
    print oinput
    print board

#    else:
#        oinput = raw_input("now O's take your turn")
#        board.insert(0, oinput)
