# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:44:34 2016

@author: sondes
compute the TMscore average of first ranking template 
"""
import os,sys
def main(argv):
    mapping=argv[1]
    modeller=argv[2]
    target_templat={}
    TMscore=[]
    pipeline=argv[3]
    for line in open(mapping):
        target=line.strip().split("\t")[0]
        template=line.split("\t")[1].split()[0].split("_")[0]        
        target_templat[target]=template
    
    for f in os.listdir(modeller):
        id=os.path.splitext(f)[0]#target name
        for key,value in target_templat.iteritems():
                if key==id:        
                    inp=os.path.join(modeller+"/"+f+"/"+target_templat[key])                    
                    for file in os.listdir(inp):
			os.chdir(inp)
                        if file.startswith("TMalign"):
				os.rename(file,modeller+"/"+f+"/"+target_templat[key]+"/"+key+"_"+target_templat[key]+file)
		                F=open(modeller+"/"+f+"/"+target_templat[key]+"/"+file).readlines()[17:19]
		                for line in F:
		                        if "Chain_1" in line:
		                           score=float(line.split()[1])
		                           TMscore.append(score)
    Average=round(sum(TMscore)/len(TMscore),3)                               
    new=open("/home/sondes/statistic","a")
    new.write("%s%s\n" % ("TM score average for the first ranked template for ",pipeline," is: ",str(Average)))                          
    new.close()                
if __name__ == "__main__":
    mapping="/home/sondes/project/Final/Modeller/modeller-hhblits/mapping"
    modeller="/home/sondes/project/Final/Modeller/modeller-hhblits"    
    main(sys.argv)
        
