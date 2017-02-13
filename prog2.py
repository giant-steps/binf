##this should solve "Rabbits and Recurrence Relations"

## run with these arguments: >python prog2.py 'n-value' 'k-value' answers.txt

##import statements
import sys

#function definitions
def rabbits(n,k):
    herd = 1
    breed = 0
    while n > 0:
        n -= 1
        young = breed * k
        breed = herd
        herd = young + breed

    return herd


##main function definition
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    with open(sys.argv[3], 'w') as out:
        out.append(rabbits(a,b))

##run main function
if __name__ == "__main__":
    main()

