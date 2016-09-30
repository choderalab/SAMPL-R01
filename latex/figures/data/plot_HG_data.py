#!/bin/env python

from numpy import *
import matplotlib
#matplotlib.use('Agg')
from pylab import *

sampl5 = loadtxt('sampl5_yin_best_HG.csv', delimiter=",")
sampl3 = loadtxt('sampl3_muddana_best_HG.csv', delimiter=",")

# Plot on same figure, initialy ignoring error bars
sampl3_x = sampl3[:,0]
sampl3_y = sampl3[:,1]
sampl5_x = sampl5[:,0]
sampl5_y = sampl5[:,1]
figure(figsize=(5,5)) #Make square
plot(sampl3_x, sampl3_y, 'bo', markersize=8)
plot(sampl5_x, sampl5_y,'yd', markersize=8)

# Find max, min of all values and adjust axis limits (same range)
highlim = ceil(max( sampl3.max(), sampl5.max()))
lowlim = floor(min( sampl3.min(), sampl5.min()))

# Add x=y line
offset = 1.5 #Offset of guide lines from x=y
plot( [lowlim, highlim], [lowlim,highlim], 'k-')
plot( [lowlim, highlim], [lowlim+offset,highlim+offset], '--', color='0.75')
plot( [lowlim, highlim], [lowlim-offset,highlim-offset], '--', color='0.75')
xlabel('Calculated binding free energy (kcal/mol)')
ylabel('Experimental binding free energy (kcal/mol)')
legend(('SAMPL3', 'SAMPL5'), loc='upper left')

# Adjust limits
xlim(lowlim, highlim)
ylim(lowlim, highlim)

# Save fig

savefig('../sampl3_and_sampl5.pdf')
