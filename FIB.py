from sys import argv
script, filename = argv
fasta = open(filename)

genes = {}
for line in fasta:
    if line.startswith(">"):
        header = line.strip(">")
        header.rstrip('\n')
        genes[header] = ""
    else:
        genes[header] += line.strip('\n')

for header,sequence in genes.items():
    count = float(sequence.count('G') + sequence.count('C'))
    gc_content = count/len(sequence) * 100    genes[header] = gc_content

print max(genes, key=genes.get)
print max(genes.values())
