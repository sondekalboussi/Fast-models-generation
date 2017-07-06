# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:54:47 2016

@author: sondes
"""
from datetime import datetime
startTime = datetime.now()
import os
def main(argv):
	input=argv[1]
	
	seqId=[]
	outp=argv[2]
	if not os.path.isdir(outp): 
 	   os.makedirs(outp)
	for f in os.listdir(inp):
    		id=os.path.splitext(f)[0]# extract the basename of the file
		query=os.path.join(inp,f)	
    		alig=outp+"/"+id+".stk"  
		unirefdb="/media/sondes/My Book/uniref90.fasta"  	
    		if not os.path.isfile(alig):  
        		os.system("jackhmmer --noali -o /dev/null -N 3 -A {ali} {query} {db}".format(ali=alig, query=query, db=unirefdb))
        new=open("/home/sondes/project/Final/statistic","a")	
	new.write("%s%s%s%s%s\n" % ("Jackhmmer running time for CASP11: ",datetime.now() - startTime," seconds"))
	new.close()
if __name__ =="__main":
	main(sys.argv)


