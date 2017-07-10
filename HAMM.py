i = 0
mut = 0
for nt in seq1:
    if seq1[i] != seq2[i]:
        mut += 1
        i += 1
print mut
