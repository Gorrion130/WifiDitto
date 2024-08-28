# Python 3
# Program to strip the macs from a csv generated by airodump-ng
# By ariakis

import sys, os, csv

# Initialise variables
separator = "Station MAC"
doPrints = False
counter = 0
targetESSID = ' ' + str(sys.argv[3])

# Navigate to the correct directory and open files for read/write
inpFilename = os.path.abspath(os.path.dirname( __file__ )) + " " + sys.argv[1]
inputFile = open(inpFilename,"r")

outFilename = os.path.abspath(os.path.dirname( __file__ )) + " " + sys.argv[2]
outputFile = open(outFilename,"a")

# Get AP's BSSID (MAC)

reader = csv.reader(inputFile)

BSSIDlist = []

for row in reader:

	if len(row) > 0: # if line not blank to prevent errs (first line is blank always)

		if row[0] == separator: # only scan APs, not clients
			break

		ESSID = row[13]

		if ESSID == targetESSID:

			BSSID = row[0]
			BSSIDlist.append(BSSID)

if len(BSSIDlist) == 0:

	print("[!] Error finding your target AP! Check the name and try again ;)")
	inputFile.close()
	outputFile.close()
	exit()

else:

	BSSIDlist = tuple(BSSIDlist) # make each element in list unique and immutable

# Main read loop

print()

for row in reader:

	if len(row) > 0: # if line not blank

		if (row[5][1:] in BSSIDlist): # if they're associated

			print(str(counter)+". "+str(row[0])) # say we've found a mac

			outputFile.write(row[0]+'\n') # write mac to file

			counter = counter + 1

print("Found",counter,"associated MAC addresses!")

inputFile.close()
outputFile.close()

