"""
Code to test input and (filtered) output of a text file.
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import matplotlib.pyplot as plt
import pandas as pd

myplace = 'ocn506/' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../../data/' + myplace

# make sure the output directory exists
out_dir = '../../output/' + myplace
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# go through the input file one line at a time
with open(in_fn, 'r', errors='ignore') as f:
    # typical real-world issue: the read operation throws an error
    # around line 383 for unknown reasons - we ignore it.
    get_data=False
    depth = [] # make empty depth list
    temp = [] # make empty temperature list
    for line in f:
        if 'END OF HEADER' in line and get_data==False:
            get_data=True
        elif get_data==True:
            LS = line.split()
            depth.append(-float(LS[1]))
            temp.append(float(LS[2]))
        
# make list into array?

# plot depth v temperature
plt.close('all')
fig=plt.figure()
plt.plot(temp,depth)
plt.show()


# practice using the pandas.csv_read fn
df = pd.read_csv(in_fn,delim_whitespace=True,skiprows=571,header=None)
fig=plt.figure()
plt.plot(df[2],-df[1])
plt.show()