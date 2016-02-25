import fileinput

## Write all results into a txt file
f = open("E:/ArcGIS/ACS/national/A_python_scripts - Copy/final_US.txt", "r")

i = 1
fout = open("output0.txt","wb")
for line in f:
	fout.write(line)
	i += 1
	if i%60000 == 0:
		fout.close()
		fout = open("output%d.txt"%(i/60000),"wb")

fout.close()  	
