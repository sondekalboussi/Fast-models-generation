# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:22:04 2016

@author: sondes
"""
import os,sys

def main(argv):
        input_fold=argv[1]
        output_folder=argv[2]
	  #pdb-id=argv[3]    
        #Filter_out=[]                
        #for line in open(pdb-id):
              #   l=line.strip().split(",")
                 #for item in l:
                   #  Filter_out.append(item)
        Map={}
        for f in os.listdir(input_fold):
            mapping={}
            Temp=[]#ordered template
            Target=[]#ordered target
            Final={}#traget sequence for the top 5 template    
            T=[]             
            id=os.path.splitext(f)[0]
            input_file=os.path.join(input_fold,f)
            #parse the sequences of the target for each of the top 5 templates           
            for line in open(input_file):
                    if line.startswith("#"):
                         no=int(line[4:].strip())
                         mapping[no]=""
                    else:  
                         mapping[no]+=line            
            for key in sorted(mapping): 
                    l= len(mapping[key].split(">"))                  
                    Target.append("".join(mapping[key].split(">")[2].split()[1:]))
                    Template=mapping[key].split(">")[l-1].split()[0]
                    #if Template not in Filter_out:
                    Temp.append(Template)
                    #else:
                        #print Template,"is new"   
            for a,b in zip(Temp[:5],Target[:5]):
                   Final[a]=b               
            Map[id]=" ".join(Temp[:5])
            for item in Temp[:5]:
                if not os.path.isdir(output_folder+"/"+id+"/"+item.split("_")[0] ):
                                            os.makedirs(output_folder+"/"+id+"/"+item.split("_")[0])  
            # mapping target-template
            New=open(output_folder+"/mapping","w")
            for key,value in Map.iteritems():        
                        New.write("%s\t%s\n" % (key,value))
            New.close()
            for key,value in Final.iteritems():
                            T=key.split("_")[0]    
                            chain=key.split("_")[1]                              
                            new=open(output_folder+"/"+id+"/"+T+"/"+id+".alig","w")
                            new.write("%s%s\n%s\n%s%s\n" %(">P1;",id,"sequence:::::::::",value,"*"))
                            new.close() 
                            #upload pdb file of the tempalte            
                            url ="http://www.ebi.ac.uk/pdbe/entry-files/pdb"+T+".ent"
                            if not os.path.exists(output_folder+"/"+id+"/"+T+"/"+"pdb"+T+".ent"):
                                os.system("wget "+url+" -P "+output_folder+"/"+id+"/"+T)
                            # write the modeller.py script
                            new=open(output_folder+"/"+id+"/"+T+"/"+"model.py","w")
                            script="""from modeller import *             
from modeller.automodel import *   
log.verbose()    
env = environ()  
env.io.atom_files= ['.', '{}']
allow_alternates=True
a = automodel(env,alnfile  ='{}.pir',knowns   ='{}',sequence = '{}')
a.starting_model= 1                
a.ending_model  = 1                                                   
a.make()""".format("pdb"+T+".ent",id+"-"+T,T,id)
                            new.write(script)
                            new.close()
                            new=open(output_folder+"/"+id+"/"+T+"/"+"align2T.py","w")
                            script="""from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='{}', model_segment=('FIRST:{}','LAST:{}'))
aln.append_model(mdl, align_codes='{}', atom_files='{}')
aln.append(file='{}', align_codes='{}')
aln.align2d()
aln.write(file='{}', alignment_format='PIR')""".format(T,chain,chain,T,"pdb"+T+".ent",id+".alig",id,id+"-"+T+".pir")
                            new.write(script)
                            new.close()
                            new=open(output_folder+"/"+id+"/"+T+"/"+"run.py","w")
                            script="""import os,sys
os.system("python {}")
os.system("python {}")""".format(output_folder+"/"+id+"/"+T+"/"+"align2T.py",output_folder+"/"+id+"/"+T+"/"+"model.py")
                            new.write(script)
                            new.close()                        
                            os.system("python "+output_folder+"/"+id+"/"+T+"/"+"run.py")#run align2T and modeller scripts
                            os.system("TMalign "+id+".B99990001.pdb "+T+".pdb > TMalign.txt")#TMscore
                            
                  
if __name__ == "__main__":
        main(sys.argv)                  
        
