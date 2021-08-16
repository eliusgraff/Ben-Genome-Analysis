import os
import csv

class organism:
    numGenes = None
    length = None
    width = None
    
    def __init__(self, *args):
        if len(args) != 3: 
            raise ValueError('Not enough info to create organism')
        self.numGenes = args[0]
        self.length = args[1]
        self.width = args[2]
        
myOrganisms = {} #dictionary
arr = os.listdir('.\GenomeFiles\\') #list of all genome files

for genomeFile in arr:
    totletter = 0
    with open('.\GenomeFiles\\' + genomeFile) as out_file:
        print( 'Input length and width for ' + genomeFile ) #get length and width of organism from user
        length = input('Length: ')
        width = input('Width: ')
        out_file.readline() #throw out top header line
        for letters in out_file:
            totletter = totletter + len(letters) - 1 #add length of string to total, subtract one for newline
        
    myOrganisms[genomeFile] = organism(totletter, length, width) #add the organism to the dict
    
#display all data
for organism in myOrganisms:
    print()
    print()
    print("For organism in :" + organism[:-4] + " file") #printing out all but last 4 charaters of filename
    print("Length: " + str(myOrganisms[organism].length) + "\tWidth: " + str(myOrganisms[organism].width))
    print("Number of Genes: " + str(myOrganisms[organism].numGenes))
    
with open('OrganismData.csv', 'w') as myFile:
    myFile.write("Organism Name,Number Of Genes,Length,Width\n")
    for organism in myOrganisms:
        myFile.write(organism + ',')
        myFile.write(str(myOrganisms[organism].numGenes) + ',')
        myFile.write(str(myOrganisms[organism].length) + ',')
        myFile.write(str(myOrganisms[organism].width) + '\n')