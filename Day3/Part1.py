from collections import Counter
from bitarray import bitarray


def byteToInt(bytesArray):
    i = 0
    for bit in bytesArray:
        i = (i << 1) | bit
    return int(i)

file = open("input Day3", "r")

convertedFile = []

gammaRate = bitarray()
epsilonRate = bitarray()

for x in range(0, 12):
    convertedLine = []
    for line in file:
        convertedLine.append(list(line)[x])
    convertedFile.append(list(convertedLine))
    file.seek(0)

for line in convertedFile:
    gammaRate.append(int(Counter(line).most_common(1)[0][0]))
    epsilonRate.append(int(Counter(line).most_common(2)[1][0]))

print(gammaRate)
print(epsilonRate)

print(byteToInt(gammaRate) * byteToInt(epsilonRate))
