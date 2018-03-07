# /usr/bin/python2.7 
# -*- coding:utf-8 -*-
import os 
#import os.path
import zipfile
import filetype

path = "./"
dex_path= "./dex/"

apklist = os.listdir(path)

if not os.path.exists(dex_path):
    os.makedirs(dex_path)
    print "[info]新增dex資料夾"

for list_dir in  os.listdir(path):
    if (os.path.isdir(list_dir)):
        if not (list_dir == "dex"):
            print "[info]搜尋資料夾底下資料進行解壓classex.dex"
            for root,dirs,files in os.walk("./"+list_dir):
                for f in files:
                    fullpath = os.path.join(root,f)
                    #print fullpath 
                    kind = filetype.guess(fullpath)
                    if kind is not None:
                        if (kind.extension == "zip"):
                            #print fullpath
                            #print kind.extension
                            zip_file = zipfile.ZipFile(fullpath,"r")
                            for unzip_file in zip_file.namelist():
                                if unzip_file.endswith(".dex"):
                                    dexfilename= f + ".dex"
                                    dexfilepath = os.path.join(dex_path,dexfilename)
                                    dexfile = open(dexfilepath,"w+")
                                    dexfile.write(zip_file.read(unzip_file))

                    #print (filetype.guess(fullpath).extension == "zip")
