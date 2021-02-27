import sys
import re

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "<code template file '.ct'>")
    sys.exit(0)

fileName = sys.argv[1]
file = open(fileName)
lines = file.readlines()


def getrange(raneAttribute):
    attributes = [];
    s = 0
    e = 0
    i = 0
    for c in raneAttribute:
        if c == "(":
            s = i + 1
        elif c == ")":
            e = i
            v = raneAttribute[s:e]
            attributes.append(v.split(","))
        i += 1
    return attributes


templateBody = []
classAttributes, ranges = [], []
for line in lines:
    if "<template class=" in line:
        # This is the line which contains template attribute
        templateBody = []
        templateAttributes = re.search('<template.*class="(.*)" range="(.*)">', line)
        classAttributes = templateAttributes.group(1)
        rangePart = templateAttributes.group(2)
        classAttributes = classAttributes.split(",")
        ranges = getrange(rangePart)
    elif "</template>" in line:
        # End of template. Process the template based on classAttributes and ranges.
        if len(classAttributes) > 0 and len(ranges) > 0:
            for r in ranges:
                for t in templateBody:
                    i = 0
                    for ar in r:
                        t = t.replace(classAttributes[i], ar)
                        i += 1
                    print(t, sep="", end="")
        classAttributes, ranges = [], []
    else:
        templateBody.append(line)
