file = open("input Day1", "r")

intList = [int(x) for x in file]
tupleList = []

for x, y, z in zip(intList, intList[1:], intList[2:]):
    tupleList.append(int(x + y + z))

print(sum(x < y for x, y in zip(tupleList, tupleList[1:])))
