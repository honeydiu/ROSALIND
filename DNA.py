sequence = raw_input("Enter nucleotide sequence: ")
A = 0
T = 0
G = 0
C = 0
nt = list(sequence)

for nt in sequence:
    if nt == "A":
        A += 1
    elif nt == "T":
        T += 1
    elif nt == "G":
        G += 1
    elif nt == "C":
        C += 1
print "%i %i %i %i" % (A,C,G,T)
