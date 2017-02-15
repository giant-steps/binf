
## this program will answer the Rosalind problem 'Consensus and Profile'

## 1st argument should be fasta input file, 2nd should be answers.txt (output file)

## import statements
import sys

## function definitions
def consensus(fastadict):
    


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
        final = consensus(sequences)
        print(str(final))
        ans.write(final)        ## may have to modify formatting here, write to output file
                                    ##line by line

## run main function
if __name__ == "__main__":
    main()