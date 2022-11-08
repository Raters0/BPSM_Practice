#!/usr/bin/python3

with open('data.csv') as obj:
    contents = obj.readlines()

print('1.1')
for line in contents:
    line = line.split(',')
    if line[0] in ['Drosophila melanogaster','Drosophila simulans']:
        print(line[2])

print('\n')
print('1.2')
for line in contents:
    line = line.split(',')
    if len(line[1]) >= 90 and len(line[1]) <= 110:
        print(line[2])

print('\n')
print('1.3')
for line in contents:
    line = line.split(',')
    AT = (line[1].lower().count('a')+line[1].lower().count('t'))/len(line[1]) 
    if AT < 0.5 and int(line[-1]) > 200:
        print(line[2])

print('\n')
print('1.4')
for line in contents:
    line = line.split(',')
    if (line[2].startswith('k') or line[2].startswith('h')) and line[0] not in ['Drosophila melanogaster']:
        print(line[2])

print('\n')
print('1.5')
for line in contents:
    line = line.split(',')
    AT = (line[1].lower().count('a')+line[1].lower().count('t'))/len(line[1])
    if AT > 0.65:
        print('AT content of '+line[2]+' is high')
    elif AT < 0.45:
        print('AT content of '+line[2]+' is low')
    else:
        print('AT content of '+line[2]+' is medium')

