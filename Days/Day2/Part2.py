file = open("input Day2", "r")

forwardCount = 0
depthCount = 0
aimCount = 0

for line in file:
    if "forward" in line:
        forwardCount += int(line.split()[1])
        depthCount += aimCount * int(line.split()[1])
    elif "down" in line:
        aimCount += int(line.split()[1])
    else:
        aimCount -= int(line.split()[1])

print("forwardCount: " + str(forwardCount))
print("depthCount: " + str(depthCount))
print("aimCount: " + str(aimCount))
print(forwardCount * depthCount)
