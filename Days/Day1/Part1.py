file = open("input Day1", "r")

intList = [int(x) for x in file]
print(sum(x < y for x, y in zip(intList, intList[1:])))
