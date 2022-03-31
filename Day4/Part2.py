# ändere Liste von Strings zu Ints
def intListConverter(stringList: list):
    stringList = list(map(int, stringList))
    return stringList

# entferne Bingoboards die gewonnen haben
# von beiden Listen
def checkEmptyLineBingoBoardWithRemove(bingoboard: list, bingoboard2: list):
    for board in bingoboard:
        for line in board:
            if not line:
                bingoboard2.remove(bingoboard2[bingoboard.index(board)])
                bingoboard.remove(board)
                break

    for board in bingoboard2:
        for line in board:
            if not line:
                bingoboard.remove(bingoboard[bingoboard2.index(board)])
                bingoboard2.remove(board)
                break

# checke ob Bingoboard leere Zeile hat
def checkEmptyLineBingoBoardWithoutRemove(bingoboard: list):
    for board in bingoboard:
        for line in board:
            if not line:
                return board
    return None


# entferne Elemente aus den Bingoboards
def elementRemoverBingoBoard(bingoBoard: list, element: int):
    for board in bingoBoard:
        for line in board:
            while element in line:
                line.remove(element)

file = open("input Day4", "r")

# 1. Zeile vom Bingoinput als Int-Liste speichern
bingoDraw = file.readline()
bingoDrawList = bingoDraw.split(",")
bingoDrawList = list(map(int, bingoDrawList))

# speichern der Bingotabellen nach Zeilen (1. Zeile wurde schon bearbeitet)
bingoBoardRowList = []
bingoBoard = []
counter = 0
for line in file:
    # überspringe leere Zeilen
    if not line.split():
        continue
    # nachdem ein volles Bingoboard erstellt wurde, füge in Liste hinzu
    # und leere Board für nächstes Board
    if counter >= 5:
        counter = 1
        bingoBoardRowList.append(bingoBoard.copy())
        bingoBoard.clear()
    else:
        counter += 1
    bingoBoard.append(line.split())

# ändere Strings zu Ints im Bingoboard
for board in bingoBoardRowList:
    for x in range(0, 5):
        board[x] = intListConverter(board[x])

# erstelle Spaltenliste von Bingoboard
bingoBoardColumnList = []
bingoBoard = []
for board in bingoBoardRowList:
    # Zeile für die Spalten erstellen
    for x in range(0, 5):
        bingoLine = []
        for line in board:
            bingoLine.append(line[x])
        bingoBoard.append(bingoLine)
    bingoBoardColumnList.append(bingoBoard.copy())
    bingoBoard.clear()

# Logik zum Bingospiel und dem Ausrechnen des Ergebnis
# checkt nicht, ob am Ende 2 Bingoboards auf einmal gewinnen
lastDraw = 0
lastBingoBoard = []
for draw in bingoDrawList:
    lastDraw = draw

    if len(bingoBoardColumnList) > 1 and len(bingoBoardRowList) > 1:
        elementRemoverBingoBoard(bingoBoardColumnList, draw)
        elementRemoverBingoBoard(bingoBoardRowList, draw)
        checkEmptyLineBingoBoardWithRemove(bingoBoardColumnList, bingoBoardRowList)

    else:
        elementRemoverBingoBoard(bingoBoardColumnList, draw)
        elementRemoverBingoBoard(bingoBoardRowList, draw)

        if checkEmptyLineBingoBoardWithoutRemove(bingoBoardColumnList) is not None:
            print("Columns are empty")
            lastBingoBoard = checkEmptyLineBingoBoardWithoutRemove(bingoBoardColumnList)
            break
        elif checkEmptyLineBingoBoardWithoutRemove(bingoBoardRowList) is not None:
            print("Rows are empty")
            lastBingoBoard = checkEmptyLineBingoBoardWithoutRemove(bingoBoardRowList)
            break

sumBingoBoard = sum(list(map(sum, lastBingoBoard)))
print(lastDraw)
print(lastBingoBoard)
print(sumBingoBoard)
print("LastDraw x sumBingoBoard: " + str(lastDraw * sumBingoBoard))
