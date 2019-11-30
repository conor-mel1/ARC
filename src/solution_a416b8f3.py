'''
Created on 30 Nov 2019

@author: conor
'''


input = [[0,5,0],[5,5,2],[0,0,0]] #This is an example of a typical input

output = [[0,5,0,0,5,0],[5,5,2,5,5,2],[0,0,0,0,0,0]] #This is an example of a typical output

output_array = [] #Defining the desired output
for grid_row in input:
    grid_row += grid_row #Adding each element on to itslef
    output_array.append(grid_row) #Appending to the output_array 
print("Correct Output Grid = ", output_array)
