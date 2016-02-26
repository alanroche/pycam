from collections import OrderedDict

encodings = {
    "S": ["TCT", "TCC", "TCA", "TCG"],
    "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
    "Y": ["TAT", "TAC"],
    "C": ["TGT", "TGC"],
}


def join(sep, array):
    return sep.join(array)


def joined(key):
    return join("", encodings[key][0])


print join("", map(joined, ["S", "Y", "L", "Y", "C"]))

a = (1, 4, 9, 16)
print list(a)

b = [4, 6, 7, 8]
print len(b[1:3])

b.append(20)
print b[-1]
print b

b.remove(6)
# print b.pop()
print b

b.extend([11, 12])
print b

b += [22, 23]
print b

b[1:2] = [100, 100, 100, 100, 100]
b.reverse()
print b

b.sort()
print b

codons = map(joined, ["C", "L", "Y", "S", "Y"])
print join(" ", codons)

start = "ATG"
stop = ""
print codons[-1]

print
print
print

text = "ATGTCATTT"
print text[0]
print text[-2]
print text[0:6]
print "ATG" in text
print "TGA" in text
print len(text)

print text

dna = "ATGTCACCGTTT"
index = dna.find("TCA")
print "TCA is at position:", index
index = dna.rfind('C')
print "The last Cytosine is at position:", index
print "Position of a stop codon:", dna.find("TGA")

print "#######################################"
str1 = "this is is really a string example....wow!!!";
str2 = "is";

print str1.rfind(str2)

print str1.rfind(str2, 0, 10)
print str1.rfind(str2, 10, 0)

print str1.find(str2)
print str1.find(str2, 0, 10)
print str1.find(str2, 10, 0)

s = "    Chromosome Start End    "
print s
print s.lstrip()
print s
s = s.strip()
print s

print codons
spaced = join(" ", codons)

print spaced

print "|".join(spaced.split(" "))

s = "chr"
chroms = [1, 2, 3]
print s + str(chroms)

name = "Bob"
age = 23
format_string = "%s is %d years old"
s = format_string % (name, age)
print s

name = "Alice"
age = 45
s = format_string % (name, age)
print s

print "Alan Roche".split(" ")[1]

print "Alan Roche".find("e")

first_name = "Alan Roche".split(" ")[0]
print "%s length is %d" % (first_name, len(first_name))

l = [1, 2, 3, 2, 3]  # list of 5 values
s = set(l)  # set of 3 unique values
print s
e = set()  # empty set
print e

print s
print "number in set:", len(s)
s.add(4)
print s
s.add(3)
s.add(3)
s.add(3)
print s

s.remove(3)
print s
e = s.pop()
print s

s1 = set([2, 4, 6, 8, 10])
s2 = set([4, 5, 6, 7, 8])

print "Union:", s1 | s2
print "Intersection:", s1 & s2

# Given the protein sequence "MPISEPTFFEIF",
# split the sequence into its component amino acid codes and use a set to establish the
# unique aminos acids in the protein.

print set("MPISEPTFFEIF")

lysozyme = "MKALIVLGLVLLSVTVQGKVFERCELARTLKRLGMDGYRGISLANWMCLAKW" \
           "ESGYNTRATNYNAGDRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDPQGIRAWVAWRNRCQNRDVRQYVQGCGV"

sorted_lysozyme = list(lysozyme)

counts_map = {}


def group(residue):
    counts_map[residue] = lysozyme.count(residue)


print map(group, set(lysozyme))
print OrderedDict(sorted(counts_map.items())).items()

dna = "ATGGCGGTCGAATAG"
if "TAG" in dna or "TAA" in dna or "TGA" in dna:
    print "HAS STOP"

for x in encodings:
    print x

basesStr = "ATGTCATTTGGACTCT"
bases = list(basesStr)

for base in bases:
    print base

# Exerise 2.1.3

print "==== Bases ==========================="
for i in xrange(2, len(bases), 3):
    print(bases[i])

print float(basesStr.count("G") + basesStr.count("C")) / 100

try:
    1 / 0

except ZeroDivisionError:
    print "divided by zero"

import math as m

print m.pi, m.e


def mean(numbers):
    return sum(numbers) / len(numbers)


print mean([5.0, 10.0, 15.0])

dna_weights = {
    "A": 331.0,
    "C": 307.0,
    "G": 347.0,
    "T": 307.0
}

rna_weights = {
    "A": 347,
    "C": 323,
    "G": 363,
    "U": 324
}
dna_weights['N'] = sum(dna_weights.values()) / len(dna_weights)
rna_weights['N'] = sum(rna_weights.values()) / len(rna_weights)

def estimate_weights(seq, seq_type="dna"):
    return sum(map(dna_weights.get if seq_type == "dna" else rna_weights.get, seq))

print "DNA Weights: ", estimate_weights("ATGGCGGTCGAATAG")
print "DNA Weights: ", estimate_weights("AUGGCGGUCGAAUAG", "rna")

assert estimate_weights("ATGGCGGTCGAATAG") == 4941.0
assert estimate_weights("AUGGCGGUCGAAUAG", "rna") == 5184

standardGeneticCode = {
          'UUU':'Phe', 'UUC':'Phe', 'UCU':'Ser', 'UCC':'Ser',
          'UAU':'Tyr', 'UAC':'Tyr', 'UGU':'Cys', 'UGC':'Cys',
          'UUA':'Leu', 'UCA':'Ser', 'UAA':None,  'UGA':None,
          'UUG':'Leu', 'UCG':'Ser', 'UAG':None,  'UGG':'Trp',
          'CUU':'Leu', 'CUC':'Leu', 'CCU':'Pro', 'CCC':'Pro',
          'CAU':'His', 'CAC':'His', 'CGU':'Arg', 'CGC':'Arg',
          'CUA':'Leu', 'CUG':'Leu', 'CCA':'Pro', 'CCG':'Pro',
          'CAA':'Gln', 'CAG':'Gln', 'CGA':'Arg', 'CGG':'Arg',
          'AUU':'Ile', 'AUC':'Ile', 'ACU':'Thr', 'ACC':'Thr',
          'AAU':'Asn', 'AAC':'Asn', 'AGU':'Ser', 'AGC':'Ser',
          'AUA':'Ile', 'ACA':'Thr', 'AAA':'Lys', 'AGA':'Arg',
          'AUG':'Met', 'ACG':'Thr', 'AAG':'Lys', 'AGG':'Arg',
          'GUU':'Val', 'GUC':'Val', 'GCU':'Ala', 'GCC':'Ala',
          'GAU':'Asp', 'GAC':'Asp', 'GGU':'Gly', 'GGC':'Gly',
          'GUA':'Val', 'GUG':'Val', 'GCA':'Ala', 'GCG':'Ala',
          'GAA':'Glu', 'GAG':'Glu', 'GGA':'Gly', 'GGG':'Gly'}

# convert_rna_to_amino_acids(rna):
#     chunks, chunk_size = len(rtn), len(x)//4
rna = "UUUUAC"

def split_by_partlen(seq, partlen, transformer):
    parts = []
    for i in xrange(0, len(seq), partlen):
        parts.append(transformer(seq[i:(i+partlen)]))
    return parts

def rna_to_aminocids(rna):
    aminoacids = []
    keys = split_by_partlen(rna, 3, lambda x: x.upper())
    for key in keys:
        aminoacids.append(standardGeneticCode[key])
    return "".join(aminoacids)

assert(rna_to_aminocids("UUUUACGGUGGGAGAGUGCAUUCGUGUUGC") == "PheTyrGlyGlyArgValHisSerCysCys")

def calculate_windows(seq, winSize, foreach_window):
    """This function takes a given sequence (seq) and a sliding window size (WinSize)
    and returns all sub-sequences acording to the size of the sliding window.
    Notice that the sub-sequences are overlapping and their size is fixed according to winSize.
    """
    if winSize <= 0:
        raise Exception("Window size must be a positive integer")
    if winSize > len(seq):
        raise Exception("Window size is larger than sequence length")
    return split_by_partlen(seq, winSize, foreach_window)

def count_gcs(seq):
    basePairs = split_by_partlen(seq, 2, lambda x: x.upper())
    return basePairs.count("GC")

assert count_gcs("ATGCGCATATATGCAT") == 3

def gc_content(seq):
    return round(float(count_gcs(seq)) / (len(seq) / 2), 4)

gc_contents = calculate_windows("ATGCGCATATATGCATAT", 6, gc_content)
print gc_contents
assert gc_contents  == [0.6667, 0.0, 0.3333]

gcResults = [0.5, 0.5, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.5, 0.6, 0.5, 0.6, 0.6, 0.6, 0.6, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 0.8, 0.7, 0.6, 0.7, 0.7, 0.7, 0.7]
print "Size: ", len(gcResults)
from matplotlib import pyplot
pyplot.plot( gcResults )
pyplot.axis([0, 50, .45, .85])
pyplot.ylabel('%GC')
pyplot.title('GC plot')
pyplot.text(12, .7, "GC Contents")
pyplot.show()