file = open("input Day5", "r")

coordinatesList = []
for line in file:
    coordniates = line.split()
    coordniates.remove("->")
    coordniates[0] = list(map(int, coordniates[0].split(",")))
    coordniates[1] = list(map(int, coordniates[1].split(",")))
    coordinatesList.append(coordniates)

print(coordinatesList)

