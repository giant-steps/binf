
import sys

## first argument is text file with some sort of whitespace separation, second argument is
    ## output file, which will contain same values but on individual lines

def main():
    with open(sys.argv[1], 'r') as start, open(sys.argv[2], 'w') as finish:
        total_list = []
        for line in start:
            linehold = []
            line = line.rstrip()
            #print(line)     ############
            linehold.append(line.split())     ### str?
            print(linehold)     ##########

            #total_list[0:0] = linehold
            for i in linehold:
                total_list.append(i)

            print(total_list)       #######################

        k = 0
        while k < len(total_list):
            finish.write(total_list[k] + '\t' + total_list[k+1])
            k += 2



if __name__ == "__main__":
    main()

