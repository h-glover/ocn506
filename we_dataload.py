"""
Homework practice with importing and manipulating data using pandas
Plot Waikaraka Estuary station data (exported from Matlab as csv)
"""

# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import glover_mod as mymod
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

# input directory
in_dir = '../../data/ocn506/'

# make sure the output directory exists
out_dir = '../../output/ocn506/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + 'WE_sedflux.csv'

# make a list of station names for cumulative sed flux:
col_names=list(['time','flux 1','flux 2','flux 3','flux 4','depth'])
flux=col_names[1:5]

# load data from csv into array and replace -999 with nans
sf = pd.read_csv(in_fn,names=col_names,header=0)
sf.index=sf['time']
# delete old time:
sf=sf.drop(columns=['time'])

# pull out the index (time) and convert to python time (cant edit index directly):
mattime = sf.index
t=[]
for jj in range (0,len(mattime)):
    t.append(mymod.datenum_to_datetime(mattime[jj]))
# replace mat time with python time:
sf.index=t
sf.index.set_names='time'

# replace -999 with nans:
sf[sf==-999]=np.nan

# calculate cumulative sediment flux (sum (sed flux*dt)):
dt = sf.index[1]-sf.index[0]
dt=dt.total_seconds()
# # make a list of station names for cumulative sed flux:
cu_flux=list(['cu flux 1','cu flux 2','cu flux 3','cu flux 4'])
sf[cu_flux]=sf[flux]*dt
sf[cu_flux]=sf[cu_flux].cumsum()


# plot the instantaneous flux and the cumulative sediment flux on two subplots:

# set default fontsize
fs = 12
plt.rc('font', size=fs)
# always start by cleaning up and setting figure size:
plt.close('all') 
fig = plt.figure(figsize=(10,6))

# first subplot is instant. sed flux:
clr = list(['darkslategray', 'g', 'lightgreen', 'chartreuse'])
ax1 = fig.add_subplot(2,1,1)
sf[flux].plot(ax=ax1,legend=False,color=clr)
ax1.set_ylim(-0.04,0.04)
ax1.set_ylabel('Instant. sediment flux (kg/s)')

# add depth to background of plot:
ax1 = ax1.twinx()
sf['depth'].plot.area(ax=ax1, color='gray',alpha=0.4,legend=False)
ax1.set_ylabel('depth', color='gray')
ax1.set_ylim(0,1.5)

ax2 = fig.add_subplot(2,1,2)
sf[cu_flux].plot(ax=ax2,color=clr)
ax2.legend(labels=['Stn 1','Stn 2','Stn 3','Stn 4'])
ax2.set_ylabel('Cumulative. sediment flux (kg)')

plt.show()

# save figure:
fig.savefig('AFTER.png')

# restore defaults
plt.rcdefaults() 
