#this program will answer Rosalind problem "Enumerating Gene Orders"

#sys.argv[1] is "n" and sys.argv[2] is answers.txt (or desired output file)

#import statements
import sys

#function definitions
def factorial(n):
    a = 1
    while n > 0:
        a = a * n
        n -= 1
    return a

def perm(n):
    return 'not complete'

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