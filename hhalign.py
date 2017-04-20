# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:33:16 2016

@author: sondes
aligne the query with each template in the mapping file and store the oyput in one file containing all the aignments
"""
import os
mapping = {}
l=[]
if not os.path.isdir("/home/sondes/Pfam_hhalign"):
    os.makedirs("/home/sondes/Pfam_hhalign")       
for l in open("/home/sondes/Mapping_Q-T").readlines():
    l=l.strip()
    query = l.split("\t")[0]
    template = l.split("\t")[1].split(" ")  
    mapping[query] = template
for F in os.listdir("/home/sondes/hhalign_input"):
    file_name=os.path.join("hhalign_input",F)
    for key in mapping:
       if not os.path.isdir("/home/sondes/Pfam_hhalign/"+key+".HMM"):
           os.makedirs("/home/sondes/Pfam_hhalign/"+key+".HMM")#craete subfolder
       for item in mapping[key]:
	if not os.path.isfile("/home/sondes/Pfam_hhalign/"+key+".HMM/"+item+".hmm"):
           f=open("/home/sondes/Pfam_hhalign/"+key+".HMM/"+item+".hmm","w")


for key in mapping:                        
    for f in os.listdir("/home/sondes/Pfam_hhalign/"+key+".HMM"):
        
        Q="/home/sondes/hhalign_input/"+key+".fa"
        
        T="/home/sondes/hhalign_input/"+f.replace(".hmm",".fa")
        O="/home/sondes/Pfam_hhalign/"+key+".HMM/"+f
        os.system("hhalign -M 50 -i {query} -t {target} -o {outp}".format(query=Q, target=T, outp=O))
             

       