sequence = raw_input("Enter nucleotide sequence: ")
motif = raw_input("Enter motif sequence: ")
locations = ""
i = 0

for i in range(len(sequence)):
    if sequence[i:i+len(motif)] == motif:
        locations += " " + str(i+1)
    i += 1

print locations
