# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:42:16 2016

@author: sondes
"""
import subprocess
G=[]#last missed entries
L=[]# entries missing in the dataset
F=[]#queries and template (full dataset)
H=[]# all the querie and templates with full seq found in uniprot 
#new=open("/home/sondes/project/input_fastpssm","w")#file contains all the input with full seq found in uniprot
#dirs=os.listdir("/home/sondes/project/uniprot fastpssm")
#for files in dirs:
#    for line in open("/home/sondes/project/uniprot fastpssm/"+files):
#        if ">" in line:
 #           new.write ("%s%s\n" %(">",line.split("|")[1]))
#        else: 
           
#            new.write(line)
 
#new.close()
            
#for line in open ("/home/sondes/project/fastpssm.txt"):
  #  if ">" in line:
 #           H.append(line[1:].strip())
#for line in open ("/home/sondes/project/queries_template.fa"):
#    if ">" in line:
 #           F.append(line[1:].strip())
#for id in F:
#    if id not in H:
 #      L.append(id)

#for id in F:
 #   if id  not in H:
 #       G.append(id)
#print G        
#new=open("/home/sondes/project/fastpssm.txt","a")
#for lines in open ("/home/sondes/project/casp11.txt"):
#    new.write(lines)
#new.close()
#cat input_fastpssm | awk '{if (substr($0,1,1)==">"){if (p){print "\n";} print $0} else printf("%s",$0);p++;}END{print "\n"}' > input_fastpssm.fasta :join wrappedf fasta line togetherby runing a command from the shell
my_proteins=['A0A077VXV8', 'A0A0C8FGT6', 'A0A0D6W4A0', 'A0A0D6W813', 'A0A0D6WFP5', 'A0A0D7NBH2', 'A0A0E2HQF9', 'C4SXS6', 'C4U606', 'E7FGN7', 'G3ZBT5', 'G6S7R4', 'M4WHW9', 'S3JG38', 'U1DE19', 'U1EFM5']
for prot in my_proteins:
    print prot
""" the entries do no longer exist in the uniprot data base deleted or under a new name"""

