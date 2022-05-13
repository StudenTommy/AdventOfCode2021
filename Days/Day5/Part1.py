file = open("input Day5", "r")

# handling Input Daten, wegstreichen von "->" und Start- und Endkoordinaten in einer Liste speichern
coordinatesList = []
for line in file:
    coordniates = line.split()
    coordniates.remove("->")
    coordniates[0] = list(map(int, coordniates[0].split(",")))
    coordniates[1] = list(map(int, coordniates[1].split(",")))
    coordinatesList.append(coordniates)

# filter Input nur nach, wenn x1 = x2 oder y1 = y2
coordinatesList = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], coordinatesList))
print(coordinatesList)

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
    else:
        start = min(lines[0][0], lines[1][0])
        end = max((lines[0][0], lines[1][0]))
        for x in range(start, end + 1):
            coordinateSystem[lines[0][1]][x] += 1

# zähle alle Schnittpunkte zusammen
sumIntersections = 0
for y in coordinateSystem:
    sumIntersections += len([elem for elem in y if elem > 1])

print(sumIntersections)
