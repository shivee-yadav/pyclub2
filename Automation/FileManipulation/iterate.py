#lines of text file that contain P

inputFile = open("Automation\FileManipulation\inputFile.txt", "r")

for line in inputFile:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
inputFile.close()