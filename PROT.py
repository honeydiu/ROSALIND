table = open("codontable.txt")
codons = {}
for i in table:
    codon,amino_acid = i.strip().split(" ")
    codons[codon] = amino_acid

sequence = raw_input("Enter nucleotide sequence: ")

i = 0
protein = ""
for nt in sequence:
    aa = sequence[i:i+3]
    if codons[aa] == "Stop":
        print protein
        break
    else:
        protein += codons[aa]
        i += 3
