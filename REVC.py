def reversed_string(string):
    return string[::-1]

def dna_complement(sequence):
    sequence = raw_input("Enter nucleotide sequence: ")
    complement = []
    nucleotides = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"
    }

    rev = reversed_string(sequence)
    nt = list(rev)

    for nt in rev:
        current_nt = nucleotides.get(nt)
        complement.append(current_nt)

    dna_complement = "".join(complement)
    print dna_complement
