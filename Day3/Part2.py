from collections import Counter

file = open("input Day3", "r")

bitList = []

for line in file:
    bitList.append(str(line.rstrip("\n")))

oxygenList = list(bitList)

while len(oxygenList) > 1:
    convertedFile = []
    prefix = ""
    # gehe jeden Bit für die jeweilgen Bitarrays durch
    for x in range(0, 12):
        convertedLine = []
        # erstelle eine Liste von dem Bits an der jeweilgen Position von x
        for line in oxygenList:
            convertedLine.append(line[x])
        convertedFile.append(convertedLine)
        # checken ob es überhaupt 2 verschiedene Bits gibt zum zählen
        if len(Counter(convertedFile[x]).most_common(2)) > 1:
            # wenn 1 und 0 gleich sind, dann setze Bit für den Prefix auf 1
            if Counter(convertedFile[x]).most_common(2)[0][1] == Counter(convertedFile[x]).most_common(2)[1][1]:
                addPrefix = "1"
            # ansonsten nehme den Bit der am meisten vorkommt
            else:
                addPrefix = str(Counter(convertedFile[x]).most_common(1)[0][0])
        # wenn es nur einen Bit zum zählen, dann nimm diesen
        else:
            addPrefix = str(Counter(convertedFile[x]).most_common(1)[0][0])
        prefix += addPrefix
        oxygenList = list(filter(lambda x: x.startswith(prefix), oxygenList))


CO2List = list(bitList)

while len(CO2List) > 1:
    convertedFile = []
    prefix = ""
    # gehe jeden Bit für die jeweilgen Bitarrays durch
    for x in range(0, 12):
        convertedLine = []
        # erstelle eine Liste von dem Bits an der jeweilgen Position von x
        for line in CO2List:
            convertedLine.append(line[x])
        convertedFile.append(convertedLine)
        # checken ob es überhaupt 2 verschiedene Bits gibt zum zählen
        if len(Counter(convertedFile[x]).most_common(2)) > 1:
            # wenn 1 und 0 gleich sind, dann setze Bit für den Prefix auf 0
            if Counter(convertedFile[x]).most_common(2)[0][1] == Counter(convertedFile[x]).most_common(2)[1][1]:
                addPrefix = "0"
            # ansonsten nehme den Bit der am wenigsten vorkommt
            else:
                addPrefix = str(Counter(convertedFile[x]).most_common(2)[1][0])
        # wenn es nur einen Bit zum zählen, dann nimm diesen
        else:
            addPrefix = str(Counter(convertedFile[x]).most_common(2)[0][0])

        prefix += addPrefix

        CO2List = list(filter(lambda x: x.startswith(prefix), CO2List))

# multipliziere die Deczimalwerte von Oxygen-Rating und CO2-Rating
print(int(oxygenList[0], 2) * int(CO2List[0], 2))


