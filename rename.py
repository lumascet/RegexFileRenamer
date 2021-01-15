import os
import sys
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tuplearray = []
p = re.compile(r'<br \/>([^\>]+)<br \/><a[^\>]*title="[^\>]*\/([a-zA-Z\s()0-9-.]+)"')

targetfolder = os.path.join("..","targets")

if not os.path.exists(targetfolder):
    os.makedirs(targetfolder)

exclude = set(['targets'])

for root, dirs, files in os.walk(".."):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        if name.endswith((".mp4")):
            oldpath = os.path.join(root, name)
            newpath = os.path.join("..","targets", name)
            os.rename(oldpath, newpath)
            print(f'{oldpath} moved to {newpath}')

with open('content.txt', encoding='utf8') as file:
    
    lines = ""

    for output in file.readlines():
        output = output.replace('&amp;', '&')
        lines += output

    results = p.findall(lines)

    for entry in results:
        print(f'Rename {entry[1]} \t to \t {entry[0]}\t')


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
    for r in results:
        try:
            print(f'Renaming {r[1]} \t to \t {r[0]+".mp4"}\t...\t\t\t',end="")
            prefix = os.path.join('..', 'targets')
            oldname = os.path.join(prefix, r[1])
            newname = os.path.join(prefix, r[0]+".mp4")
            os.rename(oldname, newname)
            print(bcolors.OKGREEN + f'Done!' + bcolors.ENDC)
        except FileNotFoundError:
            print(bcolors.WARNING +f'Missing!' + bcolors.ENDC)
            #print(f'{row[1]} not Found')
        except:
            print(bcolors.FAIL + f'Error Renaming {r[1]} \t to \t {r[0]+".mp4"}\t...\t\t\t',end="")
            print("Error:", sys.exc_info()[0] + bcolors.ENDC )


