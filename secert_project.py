import os
path = "A:\prank\prank"
'#get file names'
files = os.listdir(path)
'#Change the dir of my program to where photos are'
'#We dont need give full path to the os.rename, jsut file name and change dir to place of photos'
os.chdir(path)
'#loop throug all file and rename it'
for names in files:
    new = names.translate(None,"0123456789") 
    os.rename(names,new)


'#this method removing from String'
