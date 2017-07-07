# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:52:14 2016

@author: sondes
"""
import os,sys

def parse(lines, known):
    header = lines[0].split()[0][1:]
    if header in known:
        # We have already done this
        return
    known.append(header) 
    output = []
    for line in lines[1:]:
        if header in line:
            output.append(line.split()[3])
            
    return ''.join(output)
def main(argv):
    mapping=argv[1]#mapping file query-templates
    hhblits_output=argv[2]# output from hhblits against pdb70
    modeller_input=argv[3]# pir format files
    dataset=argv[4]#queries sequences fasta files
    New=open(mapping,"w")    
    for f in os.listdir(hhblits_output):
        input_file=os.path.join(hhblits_output,f)
        id=os.path.splitext(f)[0]
        hole_seq={}
        Map={}
        template=[]
        #parse the top 5 template with start and end match 
        for line in filter(None, open(input_file).read().split("\n")[9:]):
                    line=line.rstrip()
                    l=line.split()
                    if len(template)!=5 and l[1] not in template :
                        name=l[1]#template name
                         #begining and end of the match 
                        template.append(name.split("_")[0])
        for key in template(): 
            if not os.path.isdir(modeller_input+"/"+id+"/"+id+"_"+key.split("_")[0]):
                os.makedirs(modeller_input+"/"+id+"/"+id+"_"+key.split("_")[0]) 
            #skip all the lines that do not contain the tempalate sequence  
        Map[id]=" ".join(template)
        New.write("%s\t%s\n" % (id,Map[id]))
        known = []
        #skip the header
        input_file = open(input_file)
        for line in input_file:
            if line.startswith('>'):
                break
        lines = [line]
        parsed = []
        for line in input_file:
            if not line.startswith('>'):
                lines.append(line)
            else:
                parsed.append(parse(lines, known))
                lines = [line]
                
        parsed = filter(None, parsed)[:5]
        hole=zip(known,parsed)
        for a,b in hole:
            hole_seq[a]=b
        print hole_seq
        # writing the structure and sequence in pir format            
        for key in hole_seq.keys() :
            T=key.split("_")[0]
            new=open(modeller_input+"/"+id+"/"+id+"_"+T+"/"+key.replace(key,T)+".pir","w")  
            new.write("%s%s\n%s%s%s%s%s%s%s%s%s%s%s\n%s%s\n" % (">P1;",key.replace(key,T),"structurex:",T,"::",key.split("_")[1],"::",key.split("_")[1],"::::",hole_seq[key],"*"))
            new.close()
            for fl in os.listdir(dataset):
                id2=os.path.splitext(fl)[0]
                if id2==id:
                    new=open(modeller_input+"/"+id+"/"+id+"_"+T+"/"+key.replace(key,T)+".pir","a")
                    for line in filter(None, open(dataset+"/"+id2+".fasta").read().split("\n")):
                        if not line.startswith(">"):         os.makedirs(modeller_input+"/"+id+"/"+id+"_"+item.split("_")[0])         
        for a,b in zip(Mapping,template):
            hole_seq[a]="".join(b)
        for key in hole_seq.keys() :
                    T=key.split("_")[0]
                    new=open(modeller_input+"/"+id+"/"+T+"/"+T+".pir","w")  
                    new.write("%s%s\n%s%s%s%s%s%s%s\n%s%s\n" % (">P1;",key,"structurex:",T,"::",key.split("_")[1],"::",key.split("_")[1],"::::",hole_seq[key],"*"))
                    new.close()
                    for fl in os.listdir(dataset):
                        id2=os.path.splitext(fl)[0]
                        if id2==id:
                            new=open(modeller_input+"/"+id+"/"+id+"_"+T+"/"+key.replace(key,T)+".pir","a")
                            for line in filter(None, open(dataset+"/"+id2+".fasta").read().split("\n")):
                                if not line.startswith(">"):
                                    new.write("\n%s%s\n%s\n%s%s\n" % (">P1;",id2,"sequence:::::::::",line,"*")) 
                            new.close()       
                    #upload pdb file of the tempalte            
                    url ="http://files.rcsb.org/view/"+T+".pdb"
                    if not os.path.exists(modeller_input+"/"+id+"/"+id+"_"+T+T+".pdb"):
                        os.system("wget "+url+" -P "+modeller_input+"/"+id+"/"+id+"_"+T)
                    # write the modeller.py script
                    new=open(modeller_input+"/"+id+"/"+id+"_"+T+"/"+"model.py","w")
                    script="""from modeller import *             
        from modeller.automodel import *   
        log.verbose()    
        env = environ()  
        env.io.atom_files= ['.', '{}']
        env.io.hetatm = True
        allow_alternates=True
        a = automodel(env,alnfile  ='{}.pir',knowns   ='{}',sequence = '{}')
        a.starting_model= 1                
        a.ending_model  = 1                                                   
        a.make()""".format(T+".pdb",T,T,id)
                    new.write(script)
                    new.close()
                            new.write("\n%s%s\n%s\n%s%s\n" % (">P1;",id2,"sequence:::::::::",line,"*")) 
                    new.close()       
            #upload pdb file of the tempalte            
            url ="http://files.rcsb.org/view/"+T+".pdb"
            if not os.path.exists(modeller_input+"/"+id+"/"+id+"_"+T+T+".pdb"):
                os.system("wget "+url+" -P "+modeller_input+"/"+id+"/"+id+"_"+T)
            # write the modeller.py script
            new=open(modeller_input+"/"+id+"/"+id+"_"+T+"/"+"model.py","w")
            script="""from modeller import *             
from modeller.automodel import *   
log.verbose()    
env = environ()  
env.io.atom_files= ['.', '{}']
env.io.hetatm = True
allow_alternates=True
a = automodel(env,alnfile  ='{}.pir',knowns   ='{}',sequence = '{}')
a.starting_model= 1                
a.ending_model  = 1                                                   
a.make()""".format(T+".pdb",T,T,id)
            new.write(script)
            new.close()
                
if __name__ == "__main__":
    main(sys.argv)            
        