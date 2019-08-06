import glob, os
import shutil
import numpy as np


#######################################################################################################
#######################################################################################################
################################ USER DEFINED PARAMETERS ##############################################
#######################################################################################################
WorkDir = "D:\\__RoundRobin\\Modi_II_Tetra\\ten_node\\Script\\" # WD where all the scripts are located
NewWorkDir = "D:\\__RoundRobin\\Modi_II_Tetra\\ten_node\\Script\\" # Where you want to place the new file results folders
NameProj = "PROGETTO" # Same project name you gave in the "Sequential_File_Running.py" script
Ext = ["db", "DSP", "esav", "full", "lis", "mac", "mntr", "rst", "stat"] # Extensions you want to copy
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################


WorkDir = WorkDir.replace("\\","/")
NewWorkDir = NewWorkDir.replace("\\","/")
l=os.listdir(WorkDir) # It will listed all the files in the folder with the extension

try:
    l.remove("." + NameProj + "_files.backup") # Remove the newly created files from the WB solution
except:
    print("No file -." + NameProj + "_files.backup- found")
try:
    l.remove(NameProj + ".wbpj") # Remove the newly created files from the WB solution
except:
    print("No file -." + NameProj + ".wbpj- found")
try:
    l.remove(NameProj + "_files") # Remove the newly created files from the WB solution
except:
    print("No file -." + NameProj + "_files- found")

Scriptnames = [x.split('.')[0] for x in l] # It will listed all the files in the folder without the extension
FileNum = len(Scriptnames) # Get list length

seqvect = np.arange(0, FileNum)
seqvect = seqvect * (-1)
seqvect = list(seqvect)


for count in seqvect:
    
    if count == 0:
        srca = WorkDir + NameProj + "_files/" + "dp0/APDL/ANSYS/"
    else:
        srca = WorkDir + NameProj + "_files/" + "dp0/APDL" + str(count) + "/ANSYS/"

    os.chdir(srca)
    file = glob.glob("*.mac") # Finds the filename with extension .mac
    file = [x.split('.')[0] for x in file] # Eliminate extension
    file = ''.join(file) # Trnasaform list into string
    
    # Create directory
    dirName = NewWorkDir + file
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        
    for extension in Ext:
        if count == 0:
            src = WorkDir + NameProj + "_files/" + "dp0/APDL/ANSYS/" + file + "." + extension
        else:
            src = WorkDir + NameProj + "_files/" + "dp0/APDL" + str(count) + "/ANSYS/" + file + "." + extension
                
        newPath = shutil.copy(src, dirName, follow_symlinks=True)
