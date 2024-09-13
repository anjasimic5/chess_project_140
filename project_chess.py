# chess
# the game is played by using the left click to select a piece and the right click to select where the player wants
# the piece to move.

import math
import intrographics

# this function draws the chess board
def chessboard():
    for x in range(0, 800, 100):
        for y in range(0, 800, 100):
            polje = window.rectangle(x, y, 100, 100)
            polje.group("polja")
            if (x/100)%2 == 0 and (y/100)%2 == 0:
                color = (239,210,175)
                polje.fill(color)
            elif (x/100)%2 == 1 and (y/100)%2 == 1:
                color = (239,210,175)
                polje.fill(color)
            else:
                color = (192,104,56)
                polje.fill(color)


# this function puts the pieces on the board
def chesspieces():
    for x in range(13, 800, 100):
        whitepawn = window.image(x, 113, "belipesak.png")
        whitepawn.group("whitepawns")
        whitepawn.group("allpieces")
    for x in range(13, 800, 100):
        blackpawn = window.image(x, 613, "crnipesak.png")
        blackpawn.group("blackpawns")
        blackpawn.group("allpieces")
    for x in range(13, 800, 700):
        whiterook = window.image(x, 13, "belitop.png" )
        whiterook.group("allpieces")
        whiterook.group("rooks")
    for x in range(13, 800, 700):
        blackrook = window.image(x, 713, "crnitop.png")
        blackrook.group("allpieces")
        blackrook.group("rooks")
        blackrook.group("selected")
    for x in range(113, 800, 500):
        blackknight = window.image(x, 713, "konj.png")
        blackknight.group("allpieces")
        blackknight.group("knights")
    for x in range(113, 800, 500):
        whiteknight = window.image(x, 13, "beliskakac.png")
        whiteknight.group("allpieces")
        whiteknight.group("knights")
    for x in range(213, 800, 300):
        blackbishop = window.image(x, 713, "lovac.png")
        blackbishop.group("allpieces")
        blackbishop.group("bishops")
    for x in range(213, 800, 300):
        whitebishop = window.image(x, 13, "belilovac.png")
        whitebishop.group("allpieces")
        whitebishop.group("bishops")
    whiteking = window.image(313, 13, "belikralj.png")
    whiteking.group("allpieces")
    whiteking.group("kings")
    blackking = window.image(313, 713, "crnikralj.png")
    blackking.group("allpieces")
    blackking.group("kings")
    whitequeen = window.image(413, 13, "beladama.png")
    whitequeen.group("allpieces")
    whitequeen.group("queens")
    blackqueen = window.image(413, 713, "crnadama.png")
    blackqueen.group("allpieces")
    blackqueen.group("queens")

# this function identifies which piece the player selected
def click(x, y):
    if x <= 800:
        for piece in window.all("selected"):
             piece.ungroup("selected")
        for piece in window.all("allpieces"):
            if piece.left <= x <= piece.right and piece.top <= y <= piece.bottom:
                piece.group("selected")
                global leftside
                leftside = piece.left
                global topside
                topside = piece.top
                window.onRightClick(rightclick)
    if x > 800:
        chessclock(x, y, leftside, topside)


#this function moves the piece to the square the player clicked, and eats a piece if there was another one on that square
def rightclick(x, y):
    for polje in window.all("polja"):
        if polje.left <= x <= polje.right and polje.top <= y <= polje.bottom:
            for piece in window.all("selected"):
                piece.relocate(polje.x + 13, polje.y + 13)
                for piece2 in window.all("allpieces"):
                    if piece.overlaps(piece2):
                        piece2.group("eaten")
                        global leftside1
                        leftside1 = piece2.left
                        global piecetop1
                        piecetop1 = piece2.top
                        piece2.relocate(1000, 1000)
            # this part makes sure the pawn turns into a queen once it reaches the last row. ideally, the player
            # would be able to choose which piece appears, but as most of the time they want a queen, to simplify
            # the code I just put that the pawn automatically turns into a queen.
            for piece in window.all("selected"):
                if piece in window.all("whitepawns") and piece.top == 713:
                    newwhitequeen = window.image(piece.left, 713, "beladama.png")
                    window.remove(piece)
                    newwhitequeen.group("allpieces")
                    newwhitequeen.group("queens")
                elif piece in window.all("blackpawns") and piece.top == 13:
                    newblackqueen = window.image(piece.left, 13, "crnadama.png")
                    window.remove(piece)
                    newblackqueen.group("allpieces")
                    newblackqueen.group("queens")


#this function checks if a pawn ate a piece because pawns behave differently when they are eating from when they
# are just moving
def didpawneat():
    for piece in window.all("allpieces"):
        if piece in window.all("eaten"):
            return True
    return False


# the "chess clock" part of the design is, in this program, just used to signify the end of the move (I didnt' manage
# to actually include a timer) and once the chess clock is clicked, the program checks the validity of the move. If
# the move is not valid, the program takes the move back.
# I didn't have the time to implement all checks, but this part at least partly checks if the move is following the rules
# of how pieces are supposed to be moved. It recognizes if a piece moved in an impossible direction or for an impossible
# number of squares.
def chessclock(x, y, sideleft, piecetop):
    for piece in window.all("selected"):
        if piece in window.all("whitepawns"):
            x = didpawneat()
            if x:
                if abs(piece.left - sideleft) != 100 and (piece.top - piecetop) != -100:
                    piece.relocate(sideleft, piecetop)
            else:
                if piecetop != 113:
                    if abs(piece.left != sideleft) or abs(piece.top - piecetop)>100:
                        piece.relocate(sideleft, piecetop)
                else:
                    if abs(piece.left != sideleft) or abs(piece.top - piecetop) > 200:
                        piece.relocate(sideleft, piecetop)
        elif piece in window.all("blackpawns"):
            x = didpawneat()
            if x:
                if abs(piece.left - sideleft) != 100 and (piece.top - piecetop)!= 100:
                    piece.relocate(sideleft, piecetop)
            else:
                if piecetop != 613:
                    if abs(piece.left != leftside) or abs(piece.top - piecetop)>100:
                        piece.relocate(sideleft, piecetop)
                else:
                    if abs(piece.left != leftside) or abs(piece.top - piecetop) > 200:
                        piece.relocate(sideleft, piecetop)
        elif piece in window.all("rooks"):
            if piece.left != sideleft and piece.top != piecetop:
                piece.relocate(sideleft, piecetop)
        elif piece in window.all("bishops"):
            if (abs(piece.left - sideleft)) != (abs(piece.top - piecetop)):
                piece.relocate(sideleft, piecetop)
        elif piece in window.all("knights"):
            if (abs(piece.left - leftside) != 200 or abs(piece.top - piecetop) != 100) and (abs(piece.left - leftside) != 100 or abs(piece.top - piecetop) != 200):
                piece.relocate(sideleft, piecetop)
        elif piece in window.all("queens"):
            if (piece.left != sideleft and piece.top != piecetop) and (abs(piece.left - sideleft)) != (abs(piece.top - piecetop)):
                piece.relocate(sideleft, piecetop)
        elif piece in window.all("kings"):
            if (abs(piece.top - piecetop) > 100) or (abs(piece.left - leftside) > 100):
                piece.relocate(sideleft, piecetop)
    # this part makes sure the eaten piece reappears in the case that it being eaten was an illegal move
    for piece in window.all("selected"):
        if piece.left == sideleft and piece.top == piecetop:
            for piecegone in window.all("eaten"):
                piecegone.relocate(leftside1, piecetop1)
        else:
            for piecegone in window.all("eaten"):
                piecegone.ungroup("eaten")


# this function draws the "chess clock" in the window
def chessclockdesign():
    blackpress = window.rectangle(800, 400, 150, 400)
    blackpress.border(2, "black")
    blackpress.fill("gray")
    whitepress = window.rectangle(800, 0, 150, 400)
    whitepress.border(2, "black")
    whitepress.fill("orange")



window = intrographics.window(950, 950)

chessboard()
chessclockdesign()
chesspieces()
window.onLeftClick(click)

window.open()