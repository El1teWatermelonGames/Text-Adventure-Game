from random import choice

SUIDFormats = [16, 32, 64, 128, 256, 512, 1024, 2048]
hexCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
generatedIdentifiers = []

def main():
    while(True):
        createFile = str(input("Create a file containing the generated identifiers (y/n): "))[0].lower()
        if createFile == "y":
            createFile = True
            break
        elif createFile == "n":
            createFile = False
            break
    while(True):
        showResults = str(input("Print the all generated identifiers to the console (y/n): "))
        if showResults == "y":
            showResults = True
            break
        elif showResults == "n":
            showResults = False
            break
    while(True):
        try: SUIDFormat = int(input("SUID-"))
        except: print("Enter an integer")
        if SUIDFormat not in SUIDFormats: print("Invalid format number")
        else: break
    while(True):
        try: numbersToGenerate = int(input("How many identifiers to generate: "))
        except: print("Enter an integer")
        if type(SUIDFormat) == int:
            break
    if createFile:
        outputFile = open("SUID-Output.txt", "w")
    for count in range(numbersToGenerate):
        identifier = str(SUIDFormat) + ":"
        for i in range(int(SUIDFormat / 16)):
            for j in range(4):
                identifier = identifier + choice(hexCharacters)
            if not i == SUIDFormat / 16 - 1:
                    identifier = identifier + "-"
        if not identifier in generatedIdentifiers:
            if showResults:
                print("Progress: %s" % (count + 1) + "/%s" % numbersToGenerate + " |", identifier)
            else:
                print("Progress: %s" % (count + 1) + "/%s" % numbersToGenerate + " |", identifier, end='\r')
            if createFile == True:
                outputFile.write(identifier + "\n")
        else:
            numbersToGenerate + 1
    if createFile == True:
        outputFile.close()
    print("\nDone!")

if __name__ == "__main__":
    main()