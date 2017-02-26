
import sys

## first argument is text file with some sort of whitespace separation, second argument is
    ## output file, which will contain same values but on individual lines

def main():
    with open(sys.argv[1], 'r') as start, open(sys.argv[2], 'w') as finish:
        for line in start:
            line = line.rstrip()
            " ".join()

if __name__ == "__main__":
    main()

