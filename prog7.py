#This program will answer Rosalind problem "Inferring mRNA from Protein"

#import statements
import sys

#function definitions
def i(inp):
    decoder = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4}
        ### there are 3 possible stop codons -- you will need one at the end (multiply by 3)
    x = 3
    for a in inp:
        x = x * decoder[a]
    return x

#main function
def main():
    with open(sys.argv[1], 'r') as seq:
        d = ''
        for line in seq:
            line = line.rstrip()
            d += line
        e = i(d) % 1000000
        f = i(d)
        if f > 1000000:
            print(str(e))
        else:
            print(str(f))

#execute main function
if __name__ == "__main__":
    main()

