## Combine geo_output_US and est_output_US into one big file 

import sys, os

filenames = ['geo_output_US.txt', 'est_output_US.txt']

with open('E:/ArcGIS/ACS/national/A_python_scripts - Copy/combine_tables_US.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)