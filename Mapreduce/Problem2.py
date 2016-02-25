import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    temp = [x.encode('UTF8') for x in record]
    key = record[1]
    value =  temp   
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts       
    Join_list = []
    order = list_of_values[0]
    for i in range(len(list_of_values)-1):
		join_list = order + list_of_values[i+1]
    mr.emit((join_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
