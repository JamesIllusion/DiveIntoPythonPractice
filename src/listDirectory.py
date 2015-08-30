'''
Created on 2015-08-26

@author: James

listDirectory
'''

def listDirectory(directory, fileExtList):
    "get list of the infor objects for files of particular extensions"
    fileList=[os.path.normcase(f)
              for f in os.listdir(directory)]
    fileList=[os.path.join(directory, f)
              for f in fileList
              if os.path.splitext(f) in fileList]