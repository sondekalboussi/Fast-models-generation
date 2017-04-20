# -*- coding: utf-8 -*-


""" parse the sequences of top 5 templates"""

import os
path="/home/sondes/hhblits_uniprot_PDB_output"
dirs=os.listdir(path)
#New=os.makedirs("/home/sondes/project/hhblits_query/hhblits_output/hhblits_template")
#Pssm=open("/home/sondes/project/hhblits_query/FASTPSSM","w")


New=open("/home/sondes/map_Q-T","w")#mappinf file of queries and corresponding templates
for files in dirs:
    lines = filter(None, open(path+"/"+files).read().split("\n"))# a better way to open a file by reading the hole files lines without taking in consideration any blanks
    hole_seq ={}
    template=[]
    Map={}
    for line in lines:
        if ">tr|" in line:
            l=line.split("|")
            """ check if there is any error , a way to debug"""
            #try: 
            if l[1] not in template and len(template) !=5:
                    template.append(l[1])
                #else:
                    #break
            #except:
                #print "ERROR", line
                #exit()   
        #for i in template:
            #if "T tr|"+i in line:
              #  l=line.strip("T tr|")
             #   l=line.split()
              #  if i not in hole_seq:
              #      hole_seq[i]=l[3].replace("-","")
              #  else:
               #     hole_seq[i]+=l[3].replace("-","")
    name=files.replace(".fasta.outp","")
    #for i in template:
    Map[name]=" ".join(template)


    New.write("%s\t%s\n" % (name,Map[name]))
New.close()    	
    #new=open("/home/sondes/project/hhblits_query/hhblits_output/hhblits_template/"+files.replace(".fasta.outp","")+".temp","w")    
    #for key in hole_seq.keys():
        
        #new.write("%s%s\n%s\n" % (">",key,hole_seq[key]))
        
        #Pssm.write("%s%s\n%s\n" % (">",key,hole_seq[key]))
    #new.close()              
#Pssm.close()        
            
            
mapping = {}       
lines = filter(None, open("myfile").read().split("\n")
for line in lines:
    query = split("\t")[0]
    subjects = split("\t")[1].split(" ")   
    mapping[query] = subjects


   
            
     
       
