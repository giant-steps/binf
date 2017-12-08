

#practice creating a data structure that is a list of vectors
#then read in data (possibly from excel or .csv files) & capture in this data structure, manipulate

import numpy as np
import csv
import sys

from scipy import stats

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

    """
    reader = csv.reader(open(sys.argv[1]), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("int")
    """
    #print(str(result))

    ####
    #in data_dev_cut.csv, in column "Embarked", S = 1, C = 2, Q = 3
    #in same, 1 = male, 2 = female

    #columns are: passID, survival, pclass, sex, age, embarkation
    ###

    reader = csv.reader(open(sys.argv[1]), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("float")

    #print(str(result))

    #print(str(result[:,1]))     ### this takes the '1th' (2nd) column

    ######      NEED TO DEAL WITH MISSING DATA -- IF IGNORED, DATA WILL BE OFF -- BLANKS REPLACED W/ 0.99
            #####   I THINK ONLY AN ISSUE FOR EMBARK AND AGE

    dep_var = result[:,1]

    ###regression -- sex & survival
    ind_var_sex = result[:,3]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_sex, dep_var)
    sex_correlation = r_value**2
    print("Survival based on sex: " + (str(sex_correlation)))

    ###regression -- age & survival         FIX BLANKS ISSUE
    ind_var_age = result[:,4]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_age, dep_var)
    age_correlation = r_value**2
    #print("Survival based on age: " + (str(age_correlation)))

    ###regression -- emb & survival         FIX BLANKS ISSUE
    ind_var_emb = result[:,5]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_emb, dep_var)
    emb_correlation = r_value**2
    #print("Survival based on emb: " + (str(emb_correlation)))

    ###regression -- pclass & survival
    ind_var_pclass = result[:,2]
    slope, intercept, r_value, p_value, std_err = stats.linregress(ind_var_pclass, dep_var)
    pclass_correlation = r_value**2
    print("Survival based on social class: " + (str(pclass_correlation)))


#################

if __name__ == "__main__":
    main()

