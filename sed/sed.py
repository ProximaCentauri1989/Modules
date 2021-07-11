import sys

def printHelp():
    print("Invalid input provided\n \
    Pass path to file as first argument and replacement expression as second in format 'expression/zamena'\n \
    Example: python3 -m sed /home/docker/Documents/AWS/Connect/file.txt 'ssh/ftp'")

def readFileAndReplace(path, strToFind, replacement):
    newContent = ""
    with open(path, 'r') as file:
        for line in file:
            newContent += line.replace(strToFind, replacement)

    with open(path, 'w') as file:
        file.write(newContent)

def main():
    if len(sys.argv) < 3:
        printHelp()
        return

    path = sys.argv[1]
    arg = sys.argv[2]
    expression = arg.split(sep='/')
    if not expression or len(expression) != 2:
        printHelp()

    print("String to replace: {}".format(expression[0]))
    print("Replacement : {}".format(expression[1]))

    try:
        print("Analysis has been started...")
        readFileAndReplace(path, expression[0], expression[1])
    except Exception as err:
        print("An error occured: {}".format(err))
    else:
        print("Completed successfully")


