'''
@author: conor
'''
import json
import sys



def pattern(some_list):
    #This piece calculates the first n nonzero elements of an array
    initial_nonzero_elements = []
    for x in some_list:
        if x!=0:
            initial_nonzero_elements.append(x)

    #Way in which the patterned piece of each element of the output array is calculated
    patterned_piece = []
    for i in range(len(some_list)):
        if some_list[i]==0:
            new_list_input = some_list[i] + some_list[i-1]
            patterned_piece.append(new_list_input)

    #Combined array. Correct output grid element
    final_array = initial_nonzero_elements + patterned_piece
    return(final_array)
    
    
def solve(Input_Grid):
    Input_Grid = Input_Grid[0] #This is the only grid row within the input list of grids
    Output_Grid = []
    OutputGrid_Length = (len(Input_Grid)//2)

    for x in range(OutputGrid_Length):
        Output_GridRow = []
        Output_Grid.append(Output_GridRow)
    
    #Mapping from input grid to output grid
    Output_Grid[0] = Input_Grid 
    #This piece appplies "pattern" to each element of Output_GridArray except for Output_GridArray[0].
    i=0
    for i in range(len(Output_Grid)):
        if Output_Grid[i]!=Input_Grid:
            Output_Grid[i] = pattern(Output_Grid[i-1]) #Here the "pattern" method defined above is used to calculate elements of output grid
            i+=1
            
    for grid_row in Output_Grid:
        print("{0}".format(" ".join(str(x) for x in grid_row))) #Removing the commas from Output_Grid elements
    return(Output_Grid)

#Run the program by typing python solution_bbc9ae5d.py  \path to Json file
if len(sys.argv) != 2:
    print("usage:python solution_bbc9ae5d.py <input Json file>")
    sys.exit(0)
else:
    input_file = sys.argv[1] #This is the path to the file from the command line
    print("input_file", input_file)
    
with open(input_file) as json_file: #Loads json file into a json data structure in python 
    json_data = json.load(json_file)  
    
for i in range(len(json_data['train'])): #Specifying train input elements of the json file to apply solve method to
    solve(json_data['train'][i]['input'])
    print('\n')
    
for i in range(len(json_data['test'])):  #Specifying test input elements of the json file to apply solve method to
    solve(json_data['test'][i]['input'])
    print('\n')





    


