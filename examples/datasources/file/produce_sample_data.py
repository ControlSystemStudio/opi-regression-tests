'''
Created on May 30, 2014

A simple python script that creates a sample dataset and writes it to a file.

@author: Kunal Shroff
'''
import time
from datetime import datetime
import sys

def produceData(maxValue, numberElements):
    values = []
    for v in xrange(numberElements):
        values.append(((0.6)**(abs(v-(numberElements/2))))*maxValue)
    return values

print str(sys.argv)
output_dir = sys.argv[1]
print output_dir

nElements = 8
data_file = open(output_dir+'data_file.csv', 'wb')

labels = []
for x in xrange(nElements):
    labels.append('d'+str(x))
'''
Create the labels
'''  
data_file.write('Time,')
data_file.write(",".join(labels));
data_file.write('\n')

'''
Create 10 data sets at the rate of 1 Hz
'''
data = {}
maxValues = produceData(100,10)
for max in maxValues:
#    for i in reversed(data.keys()):
#        data[i+1] = data[i]
    
    data = produceData(max, nElements)
    '''
    write the raw data
    '''
    data_file.write(str(datetime.now())+',')
    data_file.write(",".join( map(str, data)))
    data_file.write('\n')  
    data_file.flush()
    '''
    write data in column format for plots
    '''
    col_data_file = open(output_dir+'col_data_file.csv', 'wb')
    for i in xrange(len(data)):
        col_data_file.write(str(i)+','+str(data[i])+'\n')
    col_data_file.close()    
    time.sleep(1)
    
