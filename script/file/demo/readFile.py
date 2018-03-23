import os
dir = os.getcwd()
print('Current folder: ' + dir)
print('------------------')

name = input('Please input a full file name: \n')
print('Your input file is: [' + name + ']');
print('------------------')

path = dir + '/' + name;
print('Your selected file path is: ' + path)
print('------------------')

print('------ Start Reading Files ------')
with open(path) as file:
    for line in file:
        line = line.strip()
        print(line)
print('------ End Reading Files ------')
