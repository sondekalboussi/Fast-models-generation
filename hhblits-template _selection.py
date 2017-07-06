from datetime import datetime
startTime = datetime.now()
import os,sys
def main(argv):
	input_folder=argv[1]
        output_folder=argv[2]
	db=argv[3]
	pipeline=argv[4]
	if not os.path.isdir(output_folder):
			os.makedirs(output_folder)
	for f in  os.listdir(input_folder):
		inp=os.path.join(input_folder,f)
		id=os.path.splitext(f)[0]
		out=output_folder+"/"+id+".fasta"
		os.system("hhblits -i {i} -Ofas {out} -n 1 -d {d}".format(i=inp,out=out,d=db))	
        for f in os.listdir(output_folder):
		if f.endswith(".fasta"):
		    mapping={}
		    Temp=[]#ordered template
		    Target=[]#ordered target
		    Map={}#traget and the top 5 templates                           		    
		    id=os.path.splitext(f)[0]
		    input_file=os.path.join(output_folder,f)		            
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
		            Temp.append(Template)                   
		    Map[id]=" ".join(Temp[:5]) 		    		       		  
	new=open("/home/sondes/project/Final/statistic","a")	
	new.write("%s%s%s%s%s\n" % ("Running time to get templates using ",pipeline," pipeline: ",datetime.now() - startTime," seconds"))
	new.close()
if __name__ == "__main__":
    main(sys.argv)          

	 
