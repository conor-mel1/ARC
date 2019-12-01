'''
@author: conor
'''
import sys
import json


def solve(Input_Grid):
    Output_Grid = [] 
    OutputGrid_Length = (len(Input_Grid)*2) #Defining the correct Output Grid size

    for x in range(OutputGrid_Length):
        Output_GridRow = []
        Output_Grid.append(Output_GridRow)

    #This piece applies the transfomation pattern to Input_Grid
    patterned_string = [] #Defining desired patterned grid
    for x in Input_Grid:
        y = x + x[::-1] #Create new variable y, which adds the reverse of each element of Input_Grid to itself 
        patterned_string.append(y) #Appending each y to patterned_string

    #Mapping to positions in Output Grid
    for i in range(len(Output_Grid)):
        if (i==0 or i==5):
            Output_Grid[i] = patterned_string[0]
        elif (i==1 or i==4):
            Output_Grid[i] = patterned_string[1]
        elif (i==2 or i==3):
            Output_Grid[i] = patterned_string[2]
        
    for grid_row in Output_Grid:
        print("{0}".format(" ".join(str(x) for x in grid_row))) 
    return(Output_Grid)

#Run the program at command line by typing python solution_62c24649.py  \path to Json file
if len(sys.argv) != 2:
    print("usage:python solution_62c24649.py <input Json file>")
    sys.exit(0)
else:
    input_file = sys.argv[1] #Json task file to be solved will be the first argument at command line
    print("input_file", input_file)
    
with open(input_file) as json_file: #Reading the Json file into the program 
    json_data = json.load(json_file)  
    
for i in range(len(json_data['train'])):
    solve(json_data['train'][i]['input']) #Specifying the entries of the json file to apply "solve" method to
    print('\n') #Prints a new line
    
for i in range(len(json_data['test'])):
    solve(json_data['test'][i]['input'])#Applying "solve" method to test data in the json file
    print('\n')
  

