
import sys

## first argument is text file with some sort of whitespace separation, second argument is
    ## output file, which will contain same values but on individual lines

def main():
    with open(sys.argv[1], 'r') as start, open(sys.argv[2], 'w') as finish:
        total_list = []
        for line in start:
            line = line.rstrip()
            line = line.split()

            for i in line:
                total_list.append(i)

        #print('this is total list')     ##################
        #print(total_list)                  ######################
        print(str(len(total_list)))

        k = 0
        while k < len(total_list):
            finish.write(total_list[k] + '\t' + total_list[k+1] + '\n')
            k += 2



if __name__ == "__main__":
    main()

