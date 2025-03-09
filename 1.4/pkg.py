import csv
import re
import sys


def repackage(s, packageMap):
    def getNewName(match):
        className = match.group(1)
        if className not in packageMap:
            return "net/minecraft/src/" + className
        else:
            return packageMap[className] + "/" + className

    return re.sub(r"net/minecraft/src/(\w+)", getNewName, s)


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        tokens = line.split(" ")
        kind = tokens[0]
        args = tokens[1:]
        packageMap = readCSVMap()
        if kind == "PK:":  # package
            print(line)
        elif kind == "CL:":  # class
            inName, outName = args
            print(kind, inName, repackage(outName, packageMap))
        elif kind == "FD:":  # field
            inName, outName = args
            print(kind, inName, repackage(outName, packageMap))
        elif kind == "MD:":  # method
            inName, inSig, outName, outSig = args
            print(kind, inName, inSig, repackage(outName, packageMap), repackage(outSig, packageMap))
        else:
            print(line)


def readCSVMap():
    d = {}
    header = True

    with open("packages.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if header:
                header = False
                continue
            d[row[0]] = row[1]

    return d


if __name__ == "__main__":
    main()
