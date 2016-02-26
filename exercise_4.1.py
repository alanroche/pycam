import sys
print sys.argv

assert 10 == reduce(lambda x, y: int(x) + int(y), sys.argv[1:len(sys.argv)])