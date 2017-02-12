##this will answer the following problem on Rosalind: "Overlap Graphs"

## to run, navigate to correct directory, then run: >python prog1.py sample.txt answers.txt k

##import statements
import sys


#function definitions
def overlap(fastas,k):
    ### we want to write a function that takes the last 'k' characters of a DNA sequence and checks it against the first 'k' characters of every other sequence in the fasta file
    ### every time the program finds a 'hit,' it should add keys for the pair of sequences to an adjacency list, 'edges,' as an ordered pair (first item is the key for the sequence with suffix, second item is the key for the sequence with prefix)
    k = int(k)
    edges = []  # list of ordered pairs of edges

    for f in fastas:
        hold = f            ##unnecessary, can leave hold as f
        for i in fastas:
            if hold != i:
                if fastas[hold][-k:] == fastas[i][:k]:
                    edges.append('(' + str(hold) + ', ' + str(i) + ')')

    return edges


##main function definition
def main():
    kvalue = sys.argv[3]        ### pass in an argument here that will set your k-value
    fasta_dict = {}
    with open(sys.argv[1], 'r') as input, open(sys.argv[2], 'a') as output:
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

        ans = overlap(fasta_dict, kvalue)
        for item in ans:
            output.write((item + '\n'))

###run main
if __name__ == "__main__":
    main()

