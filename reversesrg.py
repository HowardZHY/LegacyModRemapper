import sys

for line in sys.stdin.readlines():
    line = line.strip()
    tokens = line.split(" ")
    kind = tokens[0]
    args = tokens[1:]
    if kind == "PK:":
        print(line)
    elif kind == "CL:":
        if len(args) == 3:
            clin, clout, com = args
            print(kind, clout, clin, com)
        else:
            clin, clout = args
            print(kind, clout, clin)
    elif kind == "FD:":
        if len(args) == 3:
            clin, clout, com = args
            print(kind, clout, clin, com)
        else:
            clin, clout = args
            print(kind, clout, clin)
    elif kind == "MD:":
        if len(args) == 5:
            clin, descin, clout, descout, com = args
            print(kind, clout, descout, clin, descin, com)
        else:
            clin, descin, clout, descout = args
            print(kind, clout, descout, clin, descin)
    else:
        print(line)