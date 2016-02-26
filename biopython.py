from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print my_seq
print my_seq[10]
print my_seq[1:5]
print len(my_seq)
print my_seq.count( "A" )

from Bio.SeqUtils import GC, molecular_weight
print "GC: ", GC( my_seq )
print molecular_weight( my_seq )

from Bio.Alphabet import IUPAC
my_dna = Seq("AGTACATGACTGGTTTAG", IUPAC.unambiguous_dna)
print my_dna
print
print my_dna.alphabet
print my_dna.reverse_complement()

print my_dna.translate()

