import os
from objects import Result

dir = os.getcwd()
print('Current folder: ' + dir)
print('------------------')

name = input('Please input a full file name: \n')
print('Your input file is: [' + name + ']');
print('------------------')

path = dir + '/' + name;
print('Your selected file path is: ' + path)
print('------------------')

print('------ Start Reading Files ------ \n')
with open(path) as file:
    for line in file:
        line = line.strip()
        print(line)
        eles = line.split(',')
        result = Result(eles[0], eles[1], eles[2])
        print('Id: ' + result.id)
        result.toString()
print('------ End Reading Files ------')
