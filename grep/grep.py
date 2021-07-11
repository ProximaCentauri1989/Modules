import sys

def printHelp():
    print("Invalid input provided\n \
    Pass path to a file as first argument and string to find as second parameter\n \
    Example: python3 -m grep /home/docker/Documents/AWS/Connect/file.txt ssh")

def readFile(path, mode):
    with open(path, mode) as file:
        lines = file.readlines()
        return lines

def findMatch(lines, strToFind):
    return [line for line in lines if strToFind in line]

def main():
    if len(sys.argv) < 3:
        printHelp()
        return

    path = sys.argv[1]
    strToFind = sys.argv[2]

    try:
        lines = readFile(path, 'r')
    except OSError as err:
        print("Failed to read a file {}: {}".format(path, err))
    except Exception as err:
        print("An error occured: {}".format(err))
    else:
        filteredLines = findMatch(lines, strToFind)
        if not filteredLines:
            print("No lines found with '{}' in file '{}'".format(strToFind, path))
            return
        print("Lines with '{}': {}".format(strToFind, filteredLines))
