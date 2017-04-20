""" running jackhmmer and hhblits for each target from CASP11.
jackhmmer output :Stockholm alignment of HMM result
hhblits_output :HMM-HMM alignment between query and hits

"""
import os,sys
from datetime import datetime
start_time = datetime.now()
new=open("/home/sondes/time_record","w")
def main(argv):
    
    path=argv[1]#path to dataset
    hhblits_output=argv[2]#path to hhblits output folder
    Jackhmmer_output=argv[3]#path to jackhmmer output folder
    db1_path=argv[4]#path to uniprot_20
    db2_path=argv[5]#path to uniref_90
    basename=[]
    if not os.path.isdir(hhblits_output):
        os.makedirs(hhblits_output)
    if not os.path.isdir(Jackhmmer_output):
        os.makedirs(Jackhmmer_output)    
    for fl in os.listdir(path):
        id=os.path.splitext(fl)[0]# extract the basename of the file
        if id not in basename:
            basename.append(id)
            inpt=os.path.join(path,fl)
            query=inpt
            alig1=Jackhmmer_output+"/"+id+".stk"
            alig2=hhblits_output+"/"+id+".a3m"
								
            if not os.path.isfile(alig1):
       
                    os.system("jackhmmer --noali -o /dev/null -N 3 -A {ali} {query} {db}".format(ali=alig1, query=query, db=db2_path))
	
            
	    if not os.path.isfile(alig2):
		
                    os.system("hhblits -i "+inpt+" -oa3m "+alig2+" -n 1 -d "+db1_path)                
                

if __name__ == "__main__":
    main(sys.argv) 
end_time = datetime.now()

new.write('Duration: {}'.format(end_time - start_time))
new.close() 























