'''
Created on 30 Nov 2019

@author: conor
'''


def solve(input_Json):
    output_array = [] #Defining the desired output
    for grid_row in input_Json:
        grid_row += grid_row #Adding each element on to itslef
        output_array.append(grid_row) #Appending to the output_array 
    print("Output Grid = ", output_array)
    return(output_array)

#Training Data
solve([[0,5,0],[5,5,2],[0,0,0]])
solve([[3, 0, 0], [2, 3, 0], [2, 1, 8], [0, 1, 0]])
solve([[5, 2, 3, 0], [2, 5, 3, 0], [5, 2, 8, 8], [0, 0, 6, 0]])

#Testing Data
solve([[4, 0, 0, 0], [4, 5, 0, 0], [0, 5, 6, 0], [6, 6, 1, 0], [0, 0, 0, 1]])