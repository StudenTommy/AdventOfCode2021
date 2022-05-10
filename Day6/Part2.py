file = open("input Day6", "r")

# input in einer Liste speichern
fishList = list(map(int, file.readline().split(",")))


day0 = []
day1 = []
day2 = []
day3 = []
day4 = []
day5 = []
day6 = []

for x in fishList:
    if x == 0:
        day0.append(x)
    elif x == 1:
        day1.append(x)
    elif x == 2:
        day2.append(x)
    elif x == 3:
        day3.append(x)
    elif x == 4:
        day4.append(x)
    elif x == 5:
        day5.append(x)
    elif x == 6:
        day6.append(x)

lenD0 = len(day0)
lenD1 = len(day1)
lenD2 = len(day2)
lenD3 = len(day3)
lenD4 = len(day4)
lenD5 = len(day5)
lenD6 = len(day6)
lenD7 = 0
lenD8 = 0

for _ in range(256):
    babies = lenD0
    lenD0 = lenD1
    lenD1 = lenD2
    lenD2 = lenD3
    lenD3 = lenD4
    lenD4 = lenD5
    lenD5 = lenD6
    lenD6 = lenD7 + babies
    lenD7 = lenD8
    lenD8 = babies


print(lenD0 + lenD1 + lenD2 + lenD3 + lenD4 + lenD5 + lenD6 + lenD7 + lenD8)
