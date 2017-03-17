
#this program will answer the Rosalind problem "Finding a Shared Motif

## import statements
import sys

## function definitions
def shared(a):
    test = a[0]     ## test everything against 1st string
    x = 0           #########
    y = len(a[0]) - 1   #######
    count = 1       ## begin by testing 2nd string against 1st, then move to 3rd, etc.
    frame = len(a[0])       ########

    while count < len(a):   ## cycle thru all strings in list:
        if test in a[count]:       ## if this substring of test is in
            count += 1

#####   FINISHED EXCEPT FOR THIS SECTION, I THINK   ########
        else:   ## if this version of test is not in one of them, modify & start again
            count = 1   # shifts or shrinks test & starts back at beginning (of 'a')

            if y < len(a[0]):       ## if not at end then shift, else shrink by 1 & move to beginning !!!!!
                x += 1
                y += 1
            else:
                x = 0
                frame -= 1
                y = frame

        test = a[0][x:y]       ### I think this works here...it will reset test even if it needs to stay the same, but
                                ### x and y will remain unchanged so it will stay the same
##################

    return test



## main function definition
def main():
    fasta_dict = {}
    with open(sys.argv[1], 'r') as input, open(sys.argv[2], 'w') as out:
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

        ans = shared(list(fasta_dict.values()))
        out.write(ans)
        print(ans)      ###########################################


## run main function
if __name__ == "__main__":
    main()

