'''
Created on 30 Nov 2019

@author: conor
'''
import numpy as np

input = [1,1,0,0,0,0] #This is an example of a typical input

output = [[1,1,0,0,0,0],[1,1,1,0,0,0],[1,1,1,1,0,0]] #This is an example of a typical output

#def solve(input_Json):
input_Json = [1,1,0,0,0,0]
Output_GridArray = []
OutputGrid_ArrayLength = (len(input_Json)//2)

for x in range(OutputGrid_ArrayLength):
    Output_GridRow = []
    Output_GridArray.append(Output_GridRow)
print("Output Grid", Output_GridArray)
    

