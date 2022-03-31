file = open("input Day4", "r")

# 1. Zeile vom Bingoinput als Int-Liste speichern
bingoDraw = file.readline()
bingoDrawList = bingoDraw.split(",")
bingoDrawList = list(map(int, bingoDrawList))

# speichern der Bingotabellen (1. Zeile wurde schon bearbeitet)
bingoBoardList = []
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
        bingoBoardList.append(bingoBoard.copy())
        bingoBoard.clear()
    else:
        counter += 1
    bingoBoard.append(line.split())

print(bingoBoardList)