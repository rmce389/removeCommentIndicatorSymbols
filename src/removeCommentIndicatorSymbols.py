import os
import re

try:
    # ask the user what file they wish to search
    fileName = "technical_debt_dataset1"

    with open("..\\" + fileName + ".csv", "r") as file:

        # if the results file exists, delete it
        if os.path.exists("..\\Technical Debt Data - No Indicators.csv"):
            os.remove("..\\Technical Debt Data - No Indicators.csv")
        resultsFile = open("..\\Technical Debt Data - No Indicators.csv", "w")

        # read the file line-by-line
        print("Removing comment indicators...")
        for line in file:

            #remove * from the beginning of the line
            if line.startswith("*"):
                line = line[1:]

            line = re.sub(r'(//|#|/\*|\*/)', '', line)

            if not line.isspace():
                # write the non-empty line to the results file
                resultsFile.write(line)

            ##remove whitespace from the beginning of the line
            if line.startswith(" "):
               line = line[1:]

            # remove lines that only contain non-alphanumeric characters
            if not line.isalnum():
                line = line.strip()

            # write the line to the results file
            resultsFile.write(line)

        print("New lines written to file.")

except IOError:
    print("Error opening file.")
finally:
    # close the file if it is open
    if file is not None:
        file.close()
    if resultsFile is not None:
        resultsFile.close()
