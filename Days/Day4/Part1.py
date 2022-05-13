# ändere Liste von Strings zu Ints
def intListConverter(stringList: list):
    stringList = list(map(int, stringList))
    return stringList

# checke ob Bingoboard leere Zeile hat
def checkEmptyLineBingoBoard(bingoboard: list):
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
lastDraw = 0
winBingoBoard = []
for draw in bingoDrawList:
    lastDraw = draw
    elementRemoverBingoBoard(bingoBoardColumnList, draw)
    elementRemoverBingoBoard(bingoBoardRowList, draw)
    if checkEmptyLineBingoBoard(bingoBoardColumnList) is not None:
        winBingoBoard = checkEmptyLineBingoBoard(bingoBoardColumnList)
        print("Columns are empty")
        break
    elif checkEmptyLineBingoBoard(bingoBoardRowList) is not None:
        winBingoBoard = checkEmptyLineBingoBoard(bingoBoardRowList)
        print("Rows are empty")
        break

print("LastDraw: " + str(lastDraw))
print("WinBingoBoard: " + str(winBingoBoard))
sumBingoBoard = sum(list(map(sum, winBingoBoard)))
print("sumBingoBoard: " + str(sumBingoBoard))
print("LastDraw x sumBingoBoard: " + str(lastDraw * sumBingoBoard))
