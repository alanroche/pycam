import gzip
import csv
import sys

file_name = sys.argv[1]
genes_map = {}
with gzip.GzipFile( '/home/participant/1000genomes_samples.csv.gz' ) as fileObj:
    for gene in list(csv.reader( fileObj, delimiter = "," )):
        genes_map[gene[1]] = gene

with open(file_name, "r") as fileObj:
    for ( i, line ) in enumerate( fileObj):
        if genes_map[line.rstrip()]:
            print genes_map[line.rstrip()][1]
        else:
            print "Not Found", line.rstrip()