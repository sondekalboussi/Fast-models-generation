# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:15:33 2016

@author: sondes
"""
import os,sys
def main(argv):
    inpt=argv[1]
    for fl in os.listdir(inpt):
        input=os.path.join(inpt,fl)
        id1=os.path.splitext(fl)[0]
        for f in os.listdir(input):
            id=os.path.splitext(f)[0]
            new=open(input+"/"+f+"/"+"model.py","w")
            script="""from modeller import *             
from modeller.automodel import *   
log.verbose()    
env = environ()  
env.io.atom_files= ['.', '{}']
env.io.hetatm = True
allow_alternates=True
a = automodel(env,alnfile  ={}.pir,knowns   ={},sequence = {})
a.starting_model= 1                
a.ending_model  = 1                                                   
a.make()""".format(id+".pir"+".pdb","'"+id+"'","'"+id+"'","'"+id1+"'")
            new.write(script)
            new.close()

if __name__ == "__main__":
    main(sys.argv)                                
