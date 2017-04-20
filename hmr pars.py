# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:03:58 2016

@author: sondes
"""

#import os
#mapping = {}

#tem=""
#for l in open("/home/sondes/Mapping_Q-T").readlines():
 #   l=l.strip()
#    query = l.split("\t")[0].strip(" ")
#    template = l.split("\t")[1].split(" ")  
#    mapping[query] = template
#for f in os.listdir("/home/sondes/hhblits_output"):
#    for key in mapping:
 #       if not os.path.isdir("/home/sondes/project/uniprot_hhblits/"+key): 
 #           os.makedirs("/home/sondes/project/uniprot_hhblits/"+key)
 #       for item in mapping[key]:
 #           f=open("/home/sondes/project/uniprot_hhblits/"+key+"/"+item+".hmm","w")                     

f = open("/home/sondes/T0759.hmr")
count=0
intervalle=[]
for n,line in enumerate(f):
    if line.startswith(">tr|"):
       start=n
       intervalle.append(start)
       count+=1 
       
    if count== 5:
        break
for line in open("/home/sondes/T0759.hmr").readlines()[135:152]:
    print line