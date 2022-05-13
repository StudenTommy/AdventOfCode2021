file = open("input Day6", "r")

# input in einer Liste speichern
fishList = list(map(int, file.readline().split(",")))
print(fishList)
print(len(fishList))


# Algorithmenlogik
for x in range(80):
    for index in range(len(fishList)):
        if fishList[index] == 0:
            fishList[index] = 6
            fishList.append(8)
        else:
            fishList[index] -= 1

print(len(fishList))
