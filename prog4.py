
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
            if fastadict[i][counter] == 'A':
                try:
                    A[(counter + 1)] += 1
                except IndexError:
                    A[(counter + 1)] = 1
            elif fastadict[i][counter] == 'C':
                try:
                    C[(counter + 1)] += 1
                except IndexError:
                    C[(counter + 1)] = 1
            elif fastadict[i][counter] == 'G':
                try:
                    G[(counter + 1)] += 1
                except IndexError:
                    G[(counter + 1)] = 1
            elif fastadict[i][counter] == 'T':
                try:
                    T[(counter + 1)] += 1
                except IndexError:
                    T[(counter + 1)] = 1
            counter += 1

def consensus(matrix):
    l = matrix ##########################

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
        final2 = consensus(final)    ##line by line
        print('this is matrix test: ' + str(final))         #########################################
        print(str(final2))
        print(str(final))
        ans.write(str(final2))
        ans.write(final)  ## may have to modify formatting here, write to output file

## run main function
if __name__ == "__main__":
    main()

