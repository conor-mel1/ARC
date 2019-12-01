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
        Output_Grid.append(Output_GridRow)#Adding the correct number of elements to Output_Grid

    #This piece applies the transfomation pattern to Input_Grid
    patterned_elements = [] #Defining desired patterned grid
    for x in Input_Grid:
        y = x + x[::-1] #Create new variable y, which adds the reverse of each element of Input_Grid to itself #https://www.programiz.com/python-programming/methods/list/reverse`30/11/19
        patterned_elements.append(y) #Appending each y to patterned_string

    #Mapping to positions in Output Grid
    for i in range(len(Output_Grid)):
        if (i==0 or i==5):
            Output_Grid[i] = patterned_elements[0]
        elif (i==1 or i==4):
            Output_Grid[i] = patterned_elements[1]
        elif (i==2 or i==3):
            Output_Grid[i] = patterned_elements[2]
        
    for grid_row in Output_Grid:
        print("{0}".format(" ".join(str(x) for x in grid_row)))  #Removing the commas from Output_Grid elements
    return(Output_Grid) #Output of solve is also a Python list of lists

#Run the program at command line by typing python solution_62c24649.py  \path to Json file
if len(sys.argv) != 2:
    print("usage:python solution_62c24649.py <input Json file>")
    sys.exit(0)
else:
    input_file = sys.argv[1] #This is the path to the file from the command line
    #print("input_file", input_file)
    
with open(input_file) as json_file: #Loads json file into a json data structure in python 
    json_data = json.load(json_file)  
    
for i in range(len(json_data['train'])):
    solve(json_data['train'][i]['input']) #Specifying train input elements of the json file to apply solve method to
    print('\n') #Prints a new line
    
for i in range(len(json_data['test'])):
    solve(json_data['test'][i]['input']) #Specifying test input elements of the json file to apply solve method to
    print('\n')
  

