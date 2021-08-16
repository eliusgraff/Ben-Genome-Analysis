import os
import pandas as pd

if os.path.exists( 'AllData.csv' ): allData = pd.read_csv( 'AllData.csv' , index_col = 0 )
else: allData = pd.DataFrame( columns = [ 'Organism Name' , 'Num Genes' , 'Length' , 'Width'] )
arr = os.listdir('.\GenomeFiles\\') #list of all genome files

for genomeFile in arr:
    orgName = genomeFile[:-4]
    totletter = 0

    with open('.\GenomeFiles\\' + genomeFile) as out_file:
        out_file.readline() #throw out top header line

        for letters in out_file:
            totletter = totletter + len(letters) - 1 #add length of string to total, subtract one for newline

    if orgName in allData['Organism Name'].tolist(): continue

    print("adding " + orgName)
    allData = allData.append( { 'Organism Name' : orgName , 'Num Genes' : totletter} , ignore_index = True )

allData.to_csv('AllData.csv')