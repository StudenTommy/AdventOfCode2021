file = open("input Day2", "r")

forwardCount = 0
depthCount = 0

for line in file:
    if "forward" in line:
        forwardCount += int(line.split()[1])
    elif "down" in line:
        depthCount += int(line.split()[1])
    else:
        depthCount -= int(line.split()[1])

print("forwardCount: " + str(forwardCount))
print("depthCount: " + str(depthCount))
print(forwardCount * depthCount)
