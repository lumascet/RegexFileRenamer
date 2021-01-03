import os
import csv
import sys

tuplearray = []

with open('matches.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are:\n{", ".join(row)}')
            line_count += 1
        else:
            if(line_count % 2 == 1):
                tuplearray.append([])
                tuplearray[-1].append(row[5])
            else:
                tuplearray[-1].append(row[5])
                tuplearray[-1][0] += "." + tuplearray[-1][1].split(".")[-1]
            line_count += 1
    print(f'Processed {line_count} lines.')

    for row in tuplearray:
        print(f'Rename {row[1]} \t to \t {row[0]}\t')

while True: 
    query = input('Do you really want to rename all of the files listed?[N/y]:') 
    if query == '':
        answer = 'n'
        break
    elif query not in ['y','n','Y','N']: 
        print('Please answer with yes or no!') 
    else: 
        answer = query[0].lower() 
        break 
if answer == 'y': 
    for row in tuplearray:
        try:
            print(f'Renaming {row[1]} \t to \t {row[0]}\t...\t\t\t',end="")
            os.rename(row[1],row[0])
            print(f'Done!')
        except FileNotFoundError:
            None
            #print(f'{row[1]} not Found')
        except:
            print(f'Error Renaming {row[1]} \t to \t {row[0]}\t...\t\t\t',end="")
            print("Error:", sys.exc_info()[0])


