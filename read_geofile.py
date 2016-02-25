# Path = C:/Python27/ArcGIS10.2
# Path = E:/Python27
# E:/ArcGIS/ACS\national/A_python_scripts
""" This script read geofile and get a list of GEO_id and LOGRECNO """
import os, sys, csv, glob
from collections import defaultdict

## Set work place
os.chdir("E:/ArcGIS/ACS/national/A_python_scripts - Copy")

## Calculate function
def Calculate(f):
	f_result = []
	for line in f:
		""" extract  """
		list = line.split(',')
		LogRecNo = list[4]
		state = list[1]
		GEO_id = list[48][7:]
		if len(GEO_id) == 12:
			line_list = [LogRecNo, state, GEO_id]
			f_result.append(line_list)
	return f_result	

## Read file
datafile_path = "E:/ArcGIS/ACS/national/Geo_Files/*.csv"
datafile_path2 = "E:/ArcGIS/ACS/national/Geo_Files/g20125nc.csv"
		
## Loop through files  		
all_result =[]
for f_name in glob.glob(datafile_path):
	f = open(f_name, "r")
	f_result = Calculate(f)	
	#print f_result
	all_result.extend(f_result)
print len(all_result)

## Write all results into a txt file
outfile = open("geo_output_US.txt", "w")

for item in all_result:
	outfile.write(" ".join(item))
	outfile.write("\n")	
outfile.close()	