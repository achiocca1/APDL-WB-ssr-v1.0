import glob, os
import shutil

# Copy all the files with a certain extension
#######################################################################################################
#######################################################################################################
################################ USER DEFINED PARAMETERS ##############################################
#######################################################################################################
WorkDir = "D:\\__RoundRobin\\Modi_I_Tetra\\four_nodi\\" # WD where all the results folder are located
Ext = ".lis"  # Extension you want to copy
FoldName = "LIS" # Name you want to give at the folder
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################


WorkDir = WorkDir.replace("\\","/")
l=os.listdir(WorkDir) # It will listed all the files in the folder with the extension

# Make new folder for storing results
WD = WorkDir + FoldName
if not os.path.exists(WD):
    os.makedirs(WD)

for Fname in l:
    src = WorkDir + Fname 
    os.chdir(src)
    file = glob.glob("*" + Ext) # Finds the filename with extension Ext
    file = ''.join(file) # Trnasaform list into string
    
    src = src + "/" + file 
    
    newPath = shutil.copy(src, WD, follow_symlinks=True)
