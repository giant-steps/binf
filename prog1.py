##this will answer the following problem on Rosalind: "Overlap Graphs"

##import statements
import sys

"""
#function definitions
def overlap():
    a = #key in fasta_dict
    b = #key in fasta_dict
    edges = ()     #list of ordered pairs of edges
    if fasta_dict[a][-3:] == fasta_dict[b]b[:3]:
        edges.add('(' + str(a) + ', ' + str(b) + ')')

"""

##main function definition
def main():
    k = sys.argv[2]
    fasta_dict = {}
    with open(sys.argv[1], 'r') as input:
        for line in input:  # this 'for' loop reads the multifasta input file, line by line, and stores the sequences in a dictionary,
            line = line.rstrip()  # with the fasta identifiers as the dictionary keys
            if line == '':
                idstore = 'empty'
                continue
            elif line.startswith('>'):
                idstore = line
                continue
            elif idstore.startswith('>'):           #this 'try, except' setup helps if there are returns interpreted in a multi-line DNA sequence
                try:
                    if fasta_dict[idstore[1:]] == 1:
                        x = 'do nothing'
                    fasta_dict[idstore[1:]] += line
                except KeyError:
                    fasta_dict[idstore[1:]] = line
    print(fasta_dict)   ##############################################

###run main
if __name__ == "__main__":
    main()

