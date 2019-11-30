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
#print(Output_GridArray)

#This piece applies the transfomation pattern to the input_Json
patterned_string = [] #Defining desired output grid
for x in input_Json:
    y = x + x[::-1] #Create new variable y, which adds the reverse of each element of input_Json to itself 
    patterned_string.append(y) #Appending each y to patterned_string
print(patterned_string)