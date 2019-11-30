'''
@author: conor
'''

input_Json = [[3, 3, 3], [0, 2, 2], [1, 1, 0]] #This is a sample input

output = [[3, 3, 3, 3, 3, 3], [0, 2, 2, 2, 2, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 2, 2, 2, 2, 0], [3, 3, 3, 3, 3, 3]] #This is a sample output

Output_GridArray = []
OutputGrid_ArrayLength = (len(input_Json)*2)

for x in range(OutputGrid_ArrayLength):
    Output_GridRow = []
    Output_GridArray.append(Output_GridRow)
    #print(Output_GridArray)
print(Output_GridArray)