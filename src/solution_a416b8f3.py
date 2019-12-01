'''
@author: conor
'''
import json
import sys

def solve(Input_Grid):
    Output_Grid = [] #Defining the desired output
    for grid_row in Input_Grid:
        grid_row += grid_row #Adding each element on to itself
        Output_Grid.append(grid_row) #Appending to the output_array 
    
    for s in Output_Grid:
        print("{0}".format(" ".join(str(x) for x in s))) #Removing the commas from Output_Grid elements
    return(Output_Grid) #Output of solve is also a Python list of lists

#Run the program by typing python solution_a416b8f3.py  \path to Json file
#
if len(sys.argv) != 2:
    print("usage:python solution_a416b8f3.py <input Json file>")
    sys.exit(0)
else:
    input_file = sys.argv[1] #This is the path to the file from the command line
    print("input_file", input_file)
    
with open(input_file) as json_file:
    json_data = json.load(json_file) #Loads json file into a json data structure in python 
    
for i in range(len(json_data['train'])):
    solve(json_data['train'][i]['input'])#Specifying train input elements of the json file to apply solve method to
    print('\n')
    
for i in range(len(json_data['test'])):
    solve(json_data['test'][i]['input'])#Specifying test input elements of the json file to apply solve method to
    print('\n')
