# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:57:50 2016

@author: sondes
"""
import os
if not os.path.isdir("/home/sondes/project/shrinked_db"):
    os.makedirs("/home/sondes/project/shrinked_db")
for f in os.listdir("/home/sondes/project/FASTPSSM_output"):
    os.chdir("/home/sondes/project/FASTPSSM_output")
    for fl in os.listdir("/home/sondes/project/FASTPSSM_output/"+f):
        if fl.endswith(".db"):
                os.chdir("/home/sondes/project/FASTPSSM_output/"+f)
                os.rename(fl,f.replace("DIR-","")+".db")
        if fl.endswith(".fa"):
            os.chdir("/home/sondes/project/FASTPSSM_output/"+f)
            os.rename(fl,f.replace("DIR-","")+".fa")
            
        if  fl.endswith(".db") and os.path.getsize(fl) == 0: #file is not empty
                      break
        if  fl.endswith(".db") and os.path.getsize(fl) > 0: 
            src= "/home/sondes/project/FASTPSSM_output/"+f+"/"+fl
            dst="/home/sondes/project/shrinked_db/"
            os.system ("mv"+ " " + src + " " + dst)
for f in os.listdir("/home/sondes/project/shrinked_db"):
    id=os.path.splitext(f)[0]
    for fl in os.listdir("/home/sondes/project/FASTPSSM_output/DIR-"+id):
         if id in fl:
            src= "/home/sondes/project/FASTPSSM_output/DIR-"+id+"/"+id+".fa"
            dst="/home/sondes/project/shrinked_db/"
            os.system ("mv"+ " " + src + " " + dst)
