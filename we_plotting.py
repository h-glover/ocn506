"""
Plot bed stress and sediment flux in Waikaraka Estuary
"""

import sys, os
sys.path.append(os.path.abspath('shared'))
import matplotlib.pyplot as plt
import pickle
import numpy as np
from datetime import date


# file path and name for pickle with data:
in_dir = '../../output/ocn506/'
in_fn = in_dir + 'WaikarakaStns.p'

# load pickle data:
P = pickle.load(open(in_fn, 'rb')) # 'rb is for read binary
tvec=P[0]
tau=P[1]
sedflux=P[2]
sedflux_cu=P[3]
depth=P[4]

# assign station names
stns = list(['Stn 1','Stn 2','Stn 3','Stn 4'])
# assign color for each station:
clr = list(['darkslategray', 'g', 'lightgreen', 'chartreuse'])

# make the figure
fs = 10
plt.close('all') # always start by cleaning up
fig = plt.figure(figsize=(8,4))

# first subplot is bed stress
ax = fig.add_subplot(2,1,1)
for jj in range (0,len(stns)):
    ax.plot(tvec, tau[:,jj],label=stns[jj],color=clr[jj])
ax.set_ylim(0,2)
ax.set_xlim(tvec[0], tvec[-1:])
ax.set_ylabel(r'Tau (Pa)')

# add a legend and a for caption
ax.legend(fancybox=True,fontsize=fs,bbox_to_anchor=(0.8, 1),facecolor='white',framealpha=1)
ax.text(tvec[50], 1.8,'a)', fontsize=fs,color='black')

ax2 = ax.twinx()
ax2.fill_between(tvec, depth, where=(depth>0), color='gray',alpha=0.4)
ax2.set_ylabel('depth', color='gray', size=fs)
ax2.set_ylim(0,1.5)
ax2.yaxis.label.set_color('gray')

ax = fig.add_subplot(2,1,2)
# plot a zero line:
y=np.zeros((len(tvec),1))
ax.plot(tvec,y,color='black',linewidth=1)

for jj in range (0,len(stns)):
    ax.plot(tvec, sedflux[:,jj],color=clr[jj])

ax.set_ylabel(r'Sediment flux (kg/s)')
ax.set_ylim(-0.04,0.04)
ax.set_xlim(tvec[0], tvec[-1:])
# ax2 = ax.twinx()
# ax2.fill_between(tvec, depth, where=(depth>0), color='gray',alpha=0.5)
# ax2.set_ylabel('depth', color='gray', size=fs)
# ax2.set_ylim(0,1.5)

ax.text(tvec[50], 0.03,'b)', fontsize=fs,color='black')
ax.text(tvec[-1500], -0.03,'landward', fontsize=fs,color='red')
ax.text(tvec[-1500], 0.03, 'seaward', fontsize=fs,color='blue')


plt.show()
fig.savefig('AFTER.png')
