'''
@author: conor
'''
import json
import sys

def solve(Input_Grid):
    Output_Grid = [] #Defining the desired output
    for grid_row in Input_Grid:
        grid_row += grid_row #Adding each element on to itslef
        Output_Grid.append(grid_row) #Appending to the output_array 
    
    for s in Output_Grid:
        print("{0}".format(" ".join(str(x) for x in s)))
    return(Output_Grid) #Output of solve is also a Python list of lists

#Run the program by typing python solution_a416b8f3.py  \path to Json file
if len(sys.argv) != 2:
    print("usage:python solution_a416b8f3.py <input Json file>")
    sys.exit(0)
else:
    input_file = sys.argv[1]
    print("input_file", input_file)
    
with open(input_file) as json_file:
    json_data = json.load(json_file)  
    
for i in range(len(json_data['train'])):
    print("Training Output Grid ")
    solve(json_data['train'][i]['input'])#Specifying elements of the json file to apply solve method to
    print('\n')
    
for i in range(len(json_data['test'])):
    print("Testing Output Grid ")
    solve(json_data['test'][i]['input'])
    print('\n')
