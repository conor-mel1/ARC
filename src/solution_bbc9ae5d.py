'''
@author: conor
'''
import numpy as np


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
    #print("Final Patterned Array", final_array)
    return(final_array)
    
    
def solve(Input_Grid):
    Input_Grid = Input_Grid[0] #This is the only grid row within the list of grids
    Output_Grid = []
    OutputGrid_Length = (len(Input_Grid)//2)

    for x in range(OutputGrid_Length):
        Output_GridRow = []
        Output_Grid.append(Output_GridRow)
    #print(Output_GridArray)
    
    #Mapping from input grid to output grid
    Output_Grid[0] = Input_Grid #

    #This piece appplies "pattern" to each element of Output_GridArray except for Output_GridArray[0].

    i=0
    for i in range(len(Output_Grid)):
        if Output_Grid[i]!=Input_Grid:
            Output_Grid[i] = pattern(Output_Grid[i-1]) #Here the "pattern" method defined above is used to calculate elements of output grid
            i+=1
    print("Solved Output Grid = ",Output_Grid )
    return(Output_Grid)

#Training Data
solve([1,1,0,0,0,0])
solve([2, 0, 0, 0, 0, 0, 0, 0])
solve([5, 5, 5, 0, 0, 0, 0, 0, 0, 0])
solve([8, 8, 8, 8, 0, 0])
solve([7, 0, 0, 0, 0, 0])

#Testing Data
solve([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])





    


