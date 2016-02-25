# Path = C:/Python27/ArcGIS10.2

""" Value for household income from column 7 to 23  """
import os, sys, csv, glob
from collections import defaultdict

## Set work place
os.chdir("E:/ArcGIS/ACS/national/A_python_scripts - Copy")

## Helper functions
def get_sum(list):
	""" loop through a list (cannot be a string!!) and skip missing data '1','2','3','','4',..., get the sum of all values; Do NOT PUI a single number for calculating sum!!! """
	sum = 0
	if list:
		for i in list:
			if i:
				sum += float(i)
	return sum	 		# return a float number		

def calculate(f):
	result =[]
	for line in f:
		list = line.split(',')
		CBG_id =list[5]
		state = list[2].upper()
		total_pop = list[156]
		
		# # Means of Transportation to Work: (Car, truck, or van 158) + (Public transport166) + walked + Bicycle, 
		# # for total_pop = 0 or missing, use -9999
		if total_pop:	# get rid of missing values, but still have 0 value for total pop	
			total_pop = float(total_pop)
			if total_pop:
				# Car, truck, or van, col 158 
				Drive_pop = [list[157]]
				Drive_pop_perct = 100 * get_sum(Drive_pop)/total_pop
				
				# Public transport 166
				Public_pop = [list[165]]
				Public_pop_perct = 100 * get_sum(Public_pop)/total_pop
			
				# Bicycle 174
				Bicycle_pop = [list[173]]
				Bicycle_pop_perct = 100 * get_sum(Bicycle_pop)/total_pop
				
				# Walk 175
				Walk_pop = [list[174]]
				Walk_pop_perct = 100 * get_sum(Walk_pop)/total_pop
				
				# Other: Other means 176 + Taxicab 172 + Motorcycle 173
				Othermean_pop = [list[175]]
				Taxicab_pop = [list[171]]
				Motorcycle_pop = [list[172]]
				Othermean_pop = Othermean_pop + Taxicab_pop + Motorcycle_pop
				Othermean_pop_perct = 100 * get_sum(Othermean_pop)/total_pop
				
				# Work at home 177
				Home_pop = [list[176]]
				Home_pop_perct = 100 * get_sum(Home_pop)/total_pop	

				# Drive alone 159
				Drive_alone = [list[158]]	
				if get_sum(Drive_pop):
					Drive_alone_perct = 100 * get_sum(Drive_alone)/get_sum(Drive_pop)
				else:
					Drive_alone_perct = -9999

				
			else:
				Drive_pop_perct = -9999
				Public_pop_perct = -9999
				Bicycle_pop_perct = -9999
				Walk_pop_perct = -9999
				Othermean_pop_perct = -9999
				Home_pop_perct = -9999
				Drive_alone_perct = -9999
		else:
			Drive_pop_perct = -9999
			Public_pop_perct = -9999
			Bicycle_pop_perct = -9999
			Walk_pop_perct = -9999 
			Othermean_pop_perct = -9999
			Home_pop_perct = -9999
			Drive_alone_perct = -9999
			
		line_result = [CBG_id, state, str(Drive_pop_perct), str(Public_pop_perct), str(Bicycle_pop_perct),str(Walk_pop_perct), str(Othermean_pop_perct), str(Home_pop_perct), str(Drive_alone_perct), str(sum([Drive_pop_perct, Public_pop_perct, Bicycle_pop_perct, Walk_pop_perct, Othermean_pop_perct, Home_pop_perct]))]
		#print line_result
		result.append(line_result)	
	return result	

## Read input files from a dictionary 
datafile_path = "E:/ArcGIS/ACS/national/Data/e2012*0028000.txt"
datafile_path2 = "E:/ArcGIS/ACS/national/Data/e20125nc0028000.txt"

## Run tools to process the data
all_result =[]
for f_name in glob.glob(datafile_path):
	f = open(f_name, "r")
	f_result = calculate(f)	
	#print f_result
	all_result.extend(f_result)
print len(all_result)	

## Write all results into a txt file
outfile = open("est_output_US.txt", "w")

for item in all_result:
	outfile.write(" ".join(item))
	outfile.write("\n")	
outfile.close()	