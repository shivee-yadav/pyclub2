# Utilisation in python programming
# setup conditions for file creation
# verify
inputFile = open("Automation/FileManipulation/inputFile.txt", "r")

passFile = open("Automation/FileManipulation/passFile.txt", "w")#creating file to store pass test
failFile = open("Automation/FileManipulation/failFile.txt", "w")#creating file to store fail test

for line in inputFile:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

inputFile.close()
passFile.close()
failFile.close()

