# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:04:47 2016

@author: sondes

parsing .hhr files of the top 5 hits of hhblits against PDB 70 and save it in pir format for modeller with the corresponding query sequence

"""
import os,sys
def main(argv):
    #map=argv[1]#mapping file query-templates
    hhblits_output=argv[1]# output from hhblits against pdb70
    template_uniprot_pdb=argv[2]# pir format files
    dataset=argv[3]#queries sequences fasta files
    #New=open(map,"w")    
    for f in os.listdir(hhblits_output):
        input_file=os.path.join(hhblits_output,f)
        id=os.path.splitext(f)[0]
        if not os.path.isdir(template_uniprot_pdb+"/"+id):
            os.makedirs(template_uniprot_pdb+"/"+id)
        template={}
        hole_seq={}
        #Map={}
        for line in filter(None, open(input_file).read().split("\n")[9:]):
                    line=line.rstrip()
                    l=line.split()
                    if len(template)!=5 and l[1] not in template :
                        name=l[1]#template name
                        template[name]=l[-2]#begining and end of the match                  
                    for key,value in template.iteritems():
                        if line.startseith(">"+key):
                            counter=0
                            while(counter<5):
                                if "T "+key in line:
                                    line=line.strip("T ")
                                    line=line.split()
                                    if key not in hole_seq:
                                            hole_seq[key]=line[2]
                                    else:
                                            hole_seq[key]+=line[2]  
        #Map[id]=" ".join(template)
        #New.write("%s\t%s\n" % (id,Map[id]))           
        for key in hole_seq :# writing the structure and sequence in pir format
            start=template[key].split("-")[0]
            end=template[key].split("-")[1]
            new=open(template_uniprot_pdb+"/"+id+"/"+key.replace(key,key.split("_")[0])+".pir","w")  
            new.write("%s%s\n%s%s%s%s%s%s%s%s%s%s%s\n%s%s\n" % (">P1;",key.replace(key,key.split("_")[0]),"structurex:",key.split("_")[0],":",start,":",key.split("_")[1],":",end,":",key.split("_")[1],":::::",hole_seq[key],"*"))
            new.close()
            for fl in os.listdir(dataset):
                id2=os.path.splitext(fl)[0]
                if id2==id:
                    new=open(template_uniprot_pdb+"/"+id+"/"+key.replace(key,key.split("_")[0])+".pir","a")
                    for line in filter(None, open(dataset+"/"+id2+".fasta").read().split("\n")):
                        if not line.startswith(">"):
                            new.write("\n%s%s\n%s\n%s%s\n" % (">P1;",id2,"sequence:::::::::",line,"*")) 
                    new.close()    
if __name__ == "__main__":
    main(sys.argv)            
