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


def pattern(array):
    #This piece calculates the first n nonzero elements of an array
    initial_nonzero_elements = []
    for x in array:
        if x!=0:
            initial_nonzero_elements.append(x)

    #Way in which the patterned piece of each element of the output array is calculated
    patterned_piece = []
    for i in range(len(array)):
        if array[i]==0:
            new_array_input = array[i] + array[i-1]
            patterned_piece.append(new_array_input)

    #Combined array. Correct output grid element
    final_array = initial_nonzero_elements + patterned_piece
    print("Final Patterned Array", final_array)
    return(final_array)
    
pattern([1,1,1,0,0,0])

    


