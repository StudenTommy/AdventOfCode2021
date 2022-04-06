file = open("input Day5", "r")

# handling Input Daten, wegstreichen von "->" und Start- und Endkoordinaten in einer Liste speichern
coordinatesList = []
for line in file:
    coordniates = line.split()
    coordniates.remove("->")
    coordniates[0] = list(map(int, coordniates[0].split(",")))
    coordniates[1] = list(map(int, coordniates[1].split(",")))
    coordinatesList.append(coordniates)

# initialisiere Koordinatensystem
# coordinateSystem[y][x] zuerst y und dann x
coordinateSystem = [[0 for x in range(999)] for y in range(999)]

# Algorithmenlogik
for lines in coordinatesList:
    # wenn x Koordinaten gleich sind
    if lines[0][0] == lines[1][0]:
        start = min(lines[0][1], lines[1][1])
        end = max((lines[0][1], lines[1][1]))
        for y in range(start, end + 1):
            coordinateSystem[y][lines[0][0]] += 1
    # wenn y Koordinaten gleich sind
    elif lines[0][1] == lines[1][1]:
        start = min(lines[0][0], lines[1][0])
        end = max((lines[0][0], lines[1][0]))
        for x in range(start, end + 1):
            coordinateSystem[lines[0][1]][x] += 1
    # wenn Linie digaonal ist
    else:
        if lines[0][0] < lines[1][0]:
            startX = lines[0][0]
            startY = lines[0][1]
            endX = lines[1][0]
            endY = lines[1][1]
        else:
            startX = lines[1][0]
            startY = lines[1][1]
            endX = lines[0][0]
            endY = lines[0][1]
        for x in range(startX, endX + 1):
            coordinateSystem[startY][x] += 1
            if startY < endY:
                startY += 1
            elif startY > endY:
                startY -= 1


# zähle alle Schnittpunkte zusammen
sumIntersections = 0
for y in coordinateSystem:
    sumIntersections += len([elem for elem in y if elem > 1])

print(sumIntersections)
