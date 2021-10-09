 
import os
import shutil
import time

def removeFiles():
    path="C:\Users\Vedgunika\Desktop\Gunika\pics"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
       
        for rootFolder, folders, files in os.walk(path):
            
            if seconds >= getFileAge(rootFolder):
                removeFolder(rootFolder)
                break
            
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds >= getFileAge(folderPath):
                        removeFolder(folderPath)
                
                for file in files:
                    filePath=os.path.join(rootFolder, file)
                    if seconds >= getFileAge(filePath) :
                        removeFile(filePath)
        
        else:
            if seconds >=getFileAge(path):
                removeFile(path)
    
    else:
        if seconds >= getFileAge(path):
            print(path +"is not found")

def removeFolder(path):

	if not shutil.rmtree(path):

		print(path + "is removed successfully")

	else:

		print("Unable to delete the " + path)



def removeFile(path):

	if not os.remove(path):

		print(path + "is removed successfully")

	else:

		print("Unable to delete the "+ path)


def getFileAge(path):

	xtime = os.stat(path).st_xtime

	return xtime

removeFiles()