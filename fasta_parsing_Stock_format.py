import os
from stockholm_reformat import parse_fasta
if not os.path.isdir("/home/sondes/Uniprot_hhalign_input/"):
    os.makedirs("/home/sondes/Uniprot_hhalign_input/")
for f in os.listdir("/home/sondes/unip_jackhmmer"):
    id=os.path.splitext(f)[0]
    input=os.path.join("/home/sondes/unip_jackhmmer",f)
    output=open("/home/sondes/Uniprot_hhalign_input/"+id+".fa","w")
    parse_fasta(input,output)
