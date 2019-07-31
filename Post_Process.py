import os
import shutil
import numpy as np


#######################################################################################################
#######################################################################################################
################################ USER DEFINED PARAMETERS ##############################################
#######################################################################################################
WorkDir = "D:\\FIRST\\SECOND\\THIRD" # WD where all the scripts are located
NewWorkDir = "D:\\FIRST\\SECOND\\THIRD\\NEW" # Where you want to place the new file results folders
NameProj = "PROJECT" # Same project name you gave in the "Sequential_File_Running.py" script
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



for scriptname, count in zip(Scriptnames, seqvect):

    # Create directory
    dirName = NewWorkDir + scriptname
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        
    for extension in Ext:
        if count == 0:
            src = WorkDir + NameProj + "_files/" + "dp0/APDL/ANSYS/" + scriptname + "." + extension
        else:
            src = WorkDir + NameProj + "_files/" + "dp0/APDL" + str(count) + "/ANSYS/" + scriptname + "." + extension
                
        newPath = shutil.copy(src, NewWorkDir + scriptname, follow_symlinks=True)
