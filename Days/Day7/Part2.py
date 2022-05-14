import math

file = open("input Day7", "r")

crabPositions = list(map(int, file.readline().split(",")))

#crabPositions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

# nutze arithm. Mittelwert zur Berechnung der
# kosteneffizientesten Position, gehe dabei vom Minumum aus
# der gerundeten Mittelwert-Werte

lenCrabPos = len(crabPositions)
bestPositionCeil = math.ceil(sum(crabPositions) / lenCrabPos)
bestPositionFloor = math.floor(sum(crabPositions) / lenCrabPos)

fuelListCeil = list(map(lambda x: (abs(x-bestPositionCeil)*(abs(x-bestPositionCeil) + 1)) / 2, crabPositions))
fuelListFloor = list(map(lambda x: (abs(x-bestPositionFloor)*(abs(x-bestPositionFloor) + 1)) / 2, crabPositions))

print(int(sum(fuelListFloor)))
print(int(sum(fuelListCeil)))
