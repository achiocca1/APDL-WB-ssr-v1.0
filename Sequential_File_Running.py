# THIS MACRO RUN APDL SCRIPTS FROM A FOLDER THAT MUST CONTAIN ONLY THE SCRIPTS FILES.
# THE MACRO WILL CREATE A FOLDER INSIDE THE ONE IN WHICH THE SCRIPTS ARE LOCATED WITH ALL THE SOLUTIONS INSIDE
import os
import time

# You must run this script with more than one script file in the folder
#######################################################################################################
############################### USER DEFINED PARAMETERS ###############################################
#######################################################################################################
#######################################################################################################
WorkDir = "D:\\FIRST\\SECOND\\THIRD" # WD where all the scripts are located
NameProj = "PROJECT" # Project name you want to assign at the entire project of WB
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################


WorkDir = WorkDir.replace("\\","/")
#In Scriptnames you have to define the name od the ith script of the ith WorkDirectory 
l=os.listdir(WorkDir) # Import all the file name with the extension
Scriptnames = [x.split('.')[0] for x in l] # It will listed all the files in the folder without the extension

ll = l[1:] # Remove the first item from l
Scriptnames = Scriptnames[1:] # Remove the first item from Scriptnames

system = Scriptnames # Create system name variables
system.insert(0, "start_1")
del system[-1]

Scriptnames = [x.split('.')[0] for x in l]
Scriptnames = Scriptnames[1:]

setup = [x[:-1] for x in Scriptnames] # Create setup name variables

mpdaInput = [x[:-2] for x in Scriptnames] # Create mpdaInput name variables

# Open first APDL box
template1 = GetTemplate(TemplateName="Mechanical APDL")
start_1 = template1.CreateSystem()
setup1 = start_1.GetContainer(ComponentName="Setup")
mapdlInputFile1 = setup1.AddInputFile(FilePath= WorkDir + l[0] )
# Close first APDL box

# Open all the other APDL boxes
for scriptname, precscript, setupp, mpda, script in zip(Scriptnames, system, setup, mpdaInput, ll):
    
    globals()[scriptname] = eval("template1.CreateSystem(Position='Right',RelativeTo=" + precscript + ")")
    
    globals()[setupp] = eval(scriptname + ".GetContainer(ComponentName='Setup')")
    
    globals()[mpda] = eval(setupp + ".AddInputFile(FilePath=" + "'" + WorkDir +  script + "'" + ")")
# Close all the other APDL boxes

# Save the project and Run all teh scripts
Save(
    FilePath= WorkDir + NameProj + ".wbpj",
    Overwrite=True)
Update()
Save(Overwrite=True)


