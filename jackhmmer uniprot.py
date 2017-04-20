# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:12:32 2016

@author: sondes
"""
import os
for f in os.listdir("dataset"):
    id=os.path.splitext(f)[0]
    os.system("sbatch sbatch/launch_"+id+"_.bash")