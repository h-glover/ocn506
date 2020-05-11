"""
Homework practice with plotting:
Plot Waikaraka Estuary station data (exported from Matlab as csv)
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import glover_mod as mymod
import pickle
import numpy as np

# input directory
in_dir = '../../data/ocn506/'

# make sure the output directory exists
out_dir = '../../output/ocn506/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + 'WE_bedstress.csv'

# load data from csv into array and replace -999 with nans
tau = np.genfromtxt(in_fn, delimiter=',')
tau[tau==-999]=np.nan

# create a python time from the matlab time
tvec=[]
for jj in range (0, len(tau)):
    tvec.append(mymod.datenum_to_datetime(tau[jj,0]))
tau=np.delete(tau,0,1)

# load the sed flux, which has the same time stamp as the bed stress
in_fn = in_dir + 'WE_sedflux.csv'
# load data from csv into array and replace -999 with nans
sedflux = np.genfromtxt(in_fn, delimiter=',')
sedflux[sedflux==-999]=np.nan

# put depth into it's own array and delete that column and the time column:
depth=sedflux[:,5]
sedflux=np.delete(sedflux,0,1)
sedflux=np.delete(sedflux,4,1)

# calculate cumulative sediment flux (sum of sed flux*dt):
sedflux_cu=np.nancumsum(sedflux*120,1)

# save all the data as a pickle file
out_fn = out_dir + 'WaikarakaStns.p'
pickle.dump([tvec,tau,sedflux,sedflux_cu,depth], open(out_fn, 'wb'))

