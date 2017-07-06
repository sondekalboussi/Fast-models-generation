# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:22:02 2016

@author: sondes
"""
import os
from shutil import move
Id=[]
for lines in open("/home/sondes/project/missing id for psiblast").readlines():
    Id.append(lines.strip())
for f in os.listdir("/home/sondes/project/shrinked_pfamseq.db/"):
    os.chdir("/home/sondes/project/shrinked_pfamseq.db/")
    for seq in Id:
        if seq == f and ".db" not in f:
            src="/home/sondes/project/shrinked_pfamseq.db/"+f
            dst="/home/sondes/project/missing seq from pfam/"+f
            move(src,dst)#copy file
    
    
