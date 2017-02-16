
## this program will answer the Rosalind problem 'Consensus and Profile'

## 1st argument should be fasta input file, 2nd should be answers.txt (output file)

## import statements
import sys

## function definitions
def profilematrix(fastadict):
    A = []
    C = []
    G = []
    T = []
    A.append('A:')
    C.append('C:')
    G.append('G:')
    T.append('T:')
    for i in fastadict:
        counter = 0
        while counter < len(fastadict[i]):
            ######## NEW SECTION -- MAY NOT WORK --
            ######## there is a more efficient way of doing this -- this unnecessarily checks lists for zeros for every
                ########## sequence in fasta file, instead of just once
            try:
                v = A[(counter + 1)]
            except IndexError:
                A.append(0)
            try:
                v = C[(counter + 1)]
            except IndexError:
                C.append(0)
            try:
                v = G[(counter + 1)]
            except IndexError:
                G.append(0)
            try:
                v = T[(counter + 1)]
            except IndexError:
                T.append(0)
            ###########################
            if fastadict[i][counter] == 'A':
                try:
                    A[(counter + 1)] += 1
                except IndexError:
                    A.append(1)
            elif fastadict[i][counter] == 'C':
                try:
                    C[(counter + 1)] += 1
                except IndexError:
                    C.append(1)
            elif fastadict[i][counter] == 'G':
                try:
                    G[(counter + 1)] += 1
                except IndexError:
                    G.append(1)
            elif fastadict[i][counter] == 'T':
                try:
                    T[(counter + 1)] += 1
                except IndexError:
                    T.append(1)
            counter += 1
    return ' '.join(str(x) for x in A) + '\n' + ' '.join(str(x) for x in C) + '\n' + ' '.join(str(x) for x in G) + '\n' + ' '.join(str(x) for x in T)

def consensus(fastadict):
    A = []
    C = []
    G = []
    T = []
    A.append('A:')
    C.append('C:')
    G.append('G:')
    T.append('T:')
    for i in fastadict:
        counter = 0
        while counter < len(fastadict[i]):
            ######## NEW SECTION -- MAY NOT WORK --
            ######## there is a more efficient way of doing this -- this unnecessarily checks lists for zeros for every
                ########## sequence in fasta file, instead of just once
            try:
                v = A[(counter + 1)]
            except IndexError:
                A.append(0)
            try:
                v = C[(counter + 1)]
            except IndexError:
                C.append(0)
            try:
                v = G[(counter + 1)]
            except IndexError:
                G.append(0)
            try:
                v = T[(counter + 1)]
            except IndexError:
                T.append(0)
            ###########################
            if fastadict[i][counter] == 'A':
                try:
                    A[(counter + 1)] += 1
                except IndexError:
                    A.append(1)
            elif fastadict[i][counter] == 'C':
                try:
                    C[(counter + 1)] += 1
                except IndexError:
                    C.append(1)
            elif fastadict[i][counter] == 'G':
                try:
                    G[(counter + 1)] += 1
                except IndexError:
                    G.append(1)
            elif fastadict[i][counter] == 'T':
                try:
                    T[(counter + 1)] += 1
                except IndexError:
                    T.append(1)
            counter += 1

    count = 1
    common = ''
    while count < len(A):       ############# CHECK THIS
        base = 'A'
        if C[count] > A[count]:     ###### there's gotta be some max function or something to do this more efficiently
            base = 'C'
        if G[count] > A[count] and G[count] > C[count]:
            base = 'G'
        if T[count] > A[count] and T[count] > C[count] and T[count] > G[count]:
            base = 'T'
        common += base
        count += 1

    return common


## main function definition
def main():
    with open(sys.argv[1], 'r') as fasta, open(sys.argv[2], 'w') as ans:
        sequences = {}
        for line in fasta:  # this 'for' loop reads the multifasta input file, line by line, and stores the sequences in a dictionary,
            line = line.rstrip()  # with the fasta identifiers as the dictionary keys
            if line == '':
                idstore = 'empty'
                continue
            elif line.startswith('>'):
                idstore = line
                continue
            elif idstore.startswith('>'):  # this 'try, except' setup helps if there are returns interpreted in a multi-line DNA sequence
                try:
                    if sequences[str(idstore[1:])] == 1:
                        x = 'do nothing'
                    sequences[str(idstore[1:])] += line
                except KeyError:
                    sequences[str(idstore[1:])] = line
        final = profilematrix(sequences)
        final2 = consensus(sequences)    ##line by line
        ans.write(str(final2) + '\n')
        ans.write(final)

## run main function
if __name__ == "__main__":
    main()

