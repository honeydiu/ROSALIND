sequence = raw_input("Enter nucleotide sequence: ")
nt = list(sequence)

for nt in sequence:
    if nt == "T":
        rna = sequence.replace("T","U")

print rna
