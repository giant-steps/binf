

#practice creating a data structure that is a list of vectors
#then read in data (possibly from excel or .csv files) & capture in this data structure, manipulate



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
    print(str(tot))

if __name__ == "__main__":
    main()

