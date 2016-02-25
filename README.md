Use Python Script to organize and process the national data set from US Census 5 years summary big files

This folder contains scripts and text files, which demenstrate an example of processing household income data. Other types of data can be similarly processed by modifying these scripts.

Author: Yan Jiang

Last Edit Date: 2015, June
##############################################################################################

Steps:

(1). Download data from 2008-2012_ACSSF_All_In_2_Giant_Files(Experienced-Users-Only). Unpack All_Geographies_Not_Tracts_Block_Groups.tar.gz and 2012_ACS_Geography_Files.zip. All_Geographies_Not_Tracts_Block_Groups.tar.gz was called estimation file, and 2012_ACS_Geography_Files.zip was called geographic information.

(2). Yan developed python scripts to process the national datasets:
a. Read estimation file by running read_estfile.py, results were saved as est_output_US.txt.
b. Read geographic file by running read_geofile.py, results were saved as geo_output_US.txt.
c. Combine est_output_US.txt and geo_output_US.txt by running join_tables.py with Mapreduce.py in the same folder. This step generates a file final_US.txt.
d. Split the big table into small ones with 60000 rows for each one. Run split_final.py. This step generates output1.txt, output2.txt, output3.txt, output4.txt. 
e. Import the four files, output1.txt, output2.txt, output3.txt, output4.txt, into Excel 2003 file. ArcGIS 10.2 doesn’t read Excel 2013.
f. Merge output1, output2, output3, output4 tables into one table, which is the national data dbf table. Do join with national CBG layer to produce a national data layer. 
