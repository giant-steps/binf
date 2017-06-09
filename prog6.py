#this program will answer Rosalind problem "Enumerating Gene Orders"

#sys.argv[1] is "n" and sys.argv[2] is answers.txt (or desired output file)

#import statements
import sys

#function definitions
def factorial(n):
    a = 1
    n = int(n)
    while n > 0:
        a = a * n
        n -= 1
    return a

def perm(n):
    poss = ''

    count = factorial(n)
    sett = dict(range(n))
    check =

    while count > 0:
        count -= 1
        seq = {}

        for u in sett:
            if u in seq.values() == False:
                seq.append(u)

        ###should keep dictionaries and check if matches any existing -- if this permutation doesn't match any existing
            ###dictionaries, then proceed

        poss += str('\t'.join(v for v in seq)) + '\n'
    return poss


    #start a variable at factorial(n) -- this will tell you how many permutations you need
    #use a -= 1 inside a while loop: while >0: -- cycle thru
    #use an if statement: if this value that I want to put as the third element of the new sequence is not equal to
        #the third element of any existing sequences, then add
    #use dictionaries to hold sequences
    #one dictionary exists at a time (within while loop), output gets added to poss each cycle


    b = list(range(n))      ##need to add in order


#main function
def main():
    n = sys.argv[1]
    with open(sys.argv[2], 'w') as out:
        x = str(factorial(n))
        print(x)
        out.write(x + '\n')
        y = str(perm(n))
        print(y)
        out.write(y)

#execution of main function
if __name__ == "__main__":
    main()