

#practice creating a data structure that is a list of vectors
#then read in data (possibly from excel or .csv files) & capture in this data structure, manipulate

import numpy as np
import csv
import sys

def up(st):
    st += 1
    return st

def main():
    sample = [1,2,3,4,5]
    a = sample
    b = list(map(up,a))
    c = list(map(up,b))
    d = list(map(up, c))
    e = list(map(up, d))
    f = list(map(up, e))

    tot = [a,b,c,d,e,f]
    #print(str(tot))

    x = np.array(tot)

    #print(x)
    #################
    #test different items here

    #y = np.full((500,8),0)

    #print(str(y))
    #####

    #a, b, c, d, e, f, g, h, i = np.loadtxt(sys.argv[1] , skiprows=1, unpack=True)


    reader = csv.reader(open(sys.argv[1]), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("str")

    print(str(result))





#################

if __name__ == "__main__":
    main()

