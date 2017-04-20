import os
path="/home/sondes/project/casp11_target.fasta"
#Read the fasta file and store the id and the seq in a dict

Fasta={}
for lines in open(path):
        lines=lines.strip()
        if lines.startswith(">"):
            
            name=lines[1:]
            Fasta[name]=""
        else:
            
            Fasta[name]=Fasta[name]+lines
dirs=os.listdir("/home/sondes/project/hhblints_outp")    
if not os.path.isdir("/home/sondes/programs/hhblints_outp/hhblints_output"):
        os.makedirs("/home/sondes/programs/hhblints_outp/hhblints_output")
for sequence in Fasta:
        new=open("/home/sondes/programs/hhblints_outp/"+sequence+".fasta","w")
        new.write("%s%s\n%s" % (">",sequence,Fasta[sequence]))
        new.close()
    
for files in dirs:
        os.system("hhblits -i "+"/home/sondes/programs/hhblints_outp/"+files+" -o "+"/home/sondes/programs/hhblints_outp/hhblints_output/"+files+".outp -n 1 -d "+"/home/sondes/programs/hhsuite-3.0.1-Linux/uniprot20_2015_06/uniprot20_2015_06")
 
########## parsing the top 5 templates############################

 
