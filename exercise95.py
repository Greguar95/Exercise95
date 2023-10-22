fname = input('Enter file:')
try:
    fhand = open(fname)
except:
    fname = "mbox-short.txt"
    fhand = open(fname)
dc = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        eml = words[1]
        splt = eml.split('@')
        hst = splt[1]
        dc[hst] = dc.get(hst, 0) + 1
print(dc)
