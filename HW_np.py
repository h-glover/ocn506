"""
Homework for OCN506, Glover, 5/4/2020
"""

#imports
import sys, os
sys.path.append('shared')
import numpy as np
import pickle
import numpy.matlib
import my_module as mm
import matplotlib.pyplot as plt
import argparse

# use argparse to provide user input (practice!)
parser = argparse.ArgumentParser()
parser.add_argument('-cols', '--cols', default='1000', type=int)
parser.add_argument('-d','--dir_name',default='ocn506/',type=str)
args = parser.parse_args()

# number of columns must be even for the reshape line.
# Only proceed if even, else print error message
if (args.cols % 2)==0:
    # make an array 5 x cols (defined by user input):
    y = np.random.rand(5,args.cols)

    # sin(y*pi):
    y = np.sin(y*np.pi)

    # nan all values less than 0.1
    y[y<0.1]=np.nan

    # calculate the mean of each col, ignoring nans
    y_mean = np.nanmean(y,axis=0)
    y_std = np.nanstd(y,axis=0)

    # reshape y
    new_cols=args.cols//2
    y = np.reshape(y,(10,new_cols))

    # Make an x variable, same size as y:
    x = np.linspace(0,1,len(y[0]))
    x = np.matlib.repmat(x,len(y),1)

    # Multiply, element-wise
    z = np.multiply(x,y)

    # plot the first row of x vs y:
    plt.close('all')
    fig=plt.figure()
    plt.plot(x[0,:],y[0,:])
    plt.plot(x[0,:],z[0,:])
    plt.show()

    # make sure the output directory exists
    out_dir = '../../output/' + args.dir_name
    mm.make_dir(out_dir)

    # define the output filename and save as a pickle file
    out_y = out_dir + 'out_y05042020.p'
    pickle.dump(y, open(out_y, 'wb')) # 'wb' is for write binary


    # reload y with a different variable name
    y_reload = pickle.load(open(out_y, 'rb')) # 'rb is for read binary

    # check that y and y_reload are the same (ignore nans)
    if np.allclose(y,y_reload,equal_nan=True)==True:
        print('success')
    else: 
        print('keep trying')

else:
    print('number of columns must be even')