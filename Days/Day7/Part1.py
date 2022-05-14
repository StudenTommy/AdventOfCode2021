file = open("input Day7", "r")

crabPositions = list(map(int, file.readline().split(",")))

# nutze Median zur Berechnung der
# kosteneffizientesten Position

lenCrabPos = len(crabPositions)
bestPosition = sorted(crabPositions)[round(lenCrabPos / 2)]

fuelList = list(map(lambda x: abs(x-bestPosition), crabPositions))
print(sum(fuelList))
