# Ben Genome Analysis
 Code for Ben's genome analysis class
 
 Both python file and jupyter notebook included
 
Program will take all .fna files from GenomeFiles folder and count the number of genes in them.
Script will assume that all organism names are consistent with their .fna file names. Script will
compile all names and number of genes into one csv file. Length and Width can be added to the AllData.csv
file without script overwriting those cells if its run again. Program just keeps adding new organisms as
their .fna files are added to the GenomeFiles folder, always manintaing old data.