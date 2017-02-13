##this should solve "Rabbits and Recurrence Relations"

## run with these arguments: >python prog2.py 'n-value' 'k-value' answers.txt

## it takes a month for rabbits to reach breeding maturity, ALSO takes a month for young rabbits to be born
## so after 2 cycles pass, a given pair kicks in 'k' pairs of young rabbits per cycle

##import statements
import sys

#function definitions
def rabbits(n,k):
    breed = 0
    birth = 0
    young = 1
    while n > 0:
        n -= 1
        birth = birth + breed
        breed = young
        young = birth * k
        herd = young + breed + birth

    return herd

##main function definition
def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    with open(sys.argv[3], 'w') as out:
        out.write(str(rabbits(a,b)))

##run main function
if __name__ == "__main__":
    main()

