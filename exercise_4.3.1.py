import csv

genes = []
fieldnames = ['Gene', 'Chromosome', 'Start', 'Stop']

with open( "/home/participant/genes.txt", "rb" ) as fileObj:
    reader = csv.DictReader( fileObj, delimiter = "\t" ) # do no remove header
    genes.extend(list(reader))

print genes
for gene in genes:
    print gene['Gene'] + ' ' + str((int(gene['Stop']) - int(gene['Start'])))