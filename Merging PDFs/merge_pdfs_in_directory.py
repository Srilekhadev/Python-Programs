import os

# take the second element for sort
def take_second(elem):
    return int(elem.split('/')[-1].split('.')[0])

print("Python Program to print list the files in a directory.")
 
Direc = input(r"Enter the path of the folder: ")
print(f"Files in the directory: {Direc}")
 
files = os.listdir(Direc)
files = sorted([Direc+'/'+f for f in files if os.path.isfile(Direc+'/'+f)],key=take_second )#Filtering only the files.
print(*files, sep="\n")

from PyPDF2 import PdfMerger
merger = PdfMerger()
for x in files:
    merger.append(x)

merger.write(Direc+'/result.pdf')
merger.close()