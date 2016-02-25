import MapReduce
import sys

"""
Description: A Simple Python MapReduce Framework for joining two tables which share the same keys
Author: Yan Jiang
Date: July, 2014
"""

mr = MapReduce.MapReduce()

# =============================

# Mapper Function. Take input data and split into key and value pairs. 
def mapper(record):
    # key: document identifier
    # value: document contents
	#print record
	line = record.split()
	#print line, len(line)
	key = tuple([line[0],line[1]])
	
	value = line[2:]
	mr.emit_intermediate(key, value)

# Reducer function. This function will pair lines with the same key, which will accomplish a Table Join Task 
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts    
	join_list_temp = [key] 
	join_list = [join_list_temp[0][0]] 
	num_join_lists = len(list_of_values)
	#print join_list, list_of_values, num_join_lists
	if num_join_lists == 2: 
		for i in range(num_join_lists):
			join_list.extend(list_of_values[i])
		mr.emit((join_list))


# Main function
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
