
## import statements
import sys

## function definitions
def mass_sum(translate, sequence):
    window = 0
    total = 0
    while window < len(sequence):
        total += translate[sequence[window]]
        window += 1
    return total

## main function definition
    ## use aa_monoisotopicmasstable.txt as 1st argument, input.txt as 2nd, answers.txt as 3rd
def main():
    masses = {}
    aminoacid = ''
    with open(sys.argv[1], 'r') as table, open(sys.argv[2], 'r') as protein, open(sys.argv[3], 'w') as weight:
        for line in table:
            line = line.rstrip()
            masses[line[0]] = line[1]
        for line in protein:
            line = line.rstrip()
            aminoacid += str(line)
        ans = mass_sum(masses, aminoacid)
        print(str(ans))
        weight.write(str(ans))

## run main function
if __name__ == "__main__":
    main()
