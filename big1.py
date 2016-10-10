board = ["    A   ","   B   ","   C   ",
        "  ______","_______","_______",
        "1       |","       |","       ",
        "  ______","_______","_______",
        "2       |","       |","       ",
        "  ______","_______","_______",
        "3       |","       |","       ",]

def printboard():
    for idx, item in enumerate(board):
      print item,
      if idx % 3 == 2: print



def drawx(input):
    if input == "A1":
        board.pop(6)
        board.insert(6, "1   X    |")

    if input == "B1":
        board.pop(7)
        board.insert(7, "  X   |")

    if input == "C1":
        board.pop(8)
        board.insert(8, "  X   ")

    if input == "A2":
        board.pop(12)
        board.insert(12, "2   X    |")

    if input == "B2":
        board.pop(13)
        board.insert(13, "  X    |")

    if input == "C2":
        board.pop(14)
        board.insert(14, " X   ")

    if input == "A3":
        board.pop(18)
        board.insert(18, "3   X    |")

    if input == "B3":
        board.pop(19)
        board.insert(19, "  X    |")

    if input == "C3":
        board.pop(20)
        board.insert(20, " X   ")

    for idx, item in enumerate(board):
      print item,
      if idx % 3 == 2: print


def drawo(input):
    if input == "A1":
        board.pop(6)
        board.insert(6, "1   O    |")

    if input == "B1":
        board.pop(7)
        board.insert(7, "   O   |")

    if input == "C1":
        board.pop(8)
        board.insert(8, " O   ")

    if input == "A2":
        board.pop(12)
        board.insert(12, "2   O    |")

    if input == "B2":
        board.pop(13)
        board.insert(13, "   O    |")

    if input == "C2":
        board.pop(14)
        board.insert(14, " O   ")

    if input == "A3":
        board.pop(18)
        board.insert(18, "3   O    |")

    if input == "B3":
        board.pop(19)
        board.insert(19, "   O    |")

    if input == "C3":
        board.pop(20)
        board.insert(20, " O   ")

    for idx, item in enumerate(board):
      print item,
      if idx % 3 == 2: print


printboard()

for i in range(1, 10):
    xinput = raw_input("x's take your turn")
    drawx(xinput)
    printboard()
    oinput = raw_input("o take your turn")
    drawo(oinput)
    printboard()






















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
