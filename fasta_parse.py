
import sys

def parse():
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
                    if fasta_dict[str(idstore[1:])] == 1:
                        x = 'do nothing'
                    fasta_dict[str(idstore[1:])] += line
                except KeyError:
                    fasta_dict[str(idstore[1:])] = line


def main():


if __name__ == "__main__":
    main()