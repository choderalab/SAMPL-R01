#!/bin/env python

# The multibib package needs unique cite keys for things which appear in each bibliography when using numbered citations. This will process sampl-r01.bib and generate a file where "_sampl" is affixed to every cite key so it is unique.

infile = 'sampl-r01.bib'
outfile = 'sampl.bib'

file = open(infile, 'r')
text = file.readlines()
file.close()

file = open(outfile, 'w')
for idx,line in enumerate(text):
    if '@article{' in line:
        tmp = line.strip()
        #Remove trailing comma
        tmp = tmp[:-1]
        #Add sampl and trailing
        newtmp = tmp+'_sampl'
        line=line.replace(tmp, newtmp)
    file.write(line)
file.close()
