import sys
print sys.argv

seq = sys.argv[1]
def split_by_partlen(seq, partlen, transformer):
    parts = []
    for i in xrange(0, len(seq), partlen):
        parts.append(transformer(seq[i:(i+partlen)]))
    return parts

def count_gcs(seq):
    return seq.count("G") + seq.count("C")

assert count_gcs(seq) == 6

def gc_content(seq):
    return round(float(count_gcs(seq)) / (len(seq) / 2), 3)

# gc_contents = calculate_windows("ATGCGCATATATGCATAT", 6, gc_content)
print len(seq), " ", gc_content(seq)