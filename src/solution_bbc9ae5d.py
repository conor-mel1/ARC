'''
@author: conor
'''
import numpy as np


#def solve(input_Json):
input_Json = [1,1,0,0,0,0]
Output_GridArray = []
OutputGrid_ArrayLength = (len(input_Json)//2)

for x in range(OutputGrid_ArrayLength):
    Output_GridRow = []
    Output_GridArray.append(Output_GridRow)
print("Output Grid", Output_GridArray)

#This piece calculates the first n nonzero elements of an array
array = [1,1,0,0,0,0]
initial_nonzero_elements = []
for x in array:
    if x!=0:
        initial_nonzero_elements.append(x)
print(initial_nonzero_elements)

    
    


