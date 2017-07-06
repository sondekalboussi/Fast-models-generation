# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:09:19 2016

@author: sondes
"""
from Bio import SeqIO
import os

if not os.path.isdir("hhalign_input"):
    os.makedirs("hhalign_input")
for f in os.listdir("pfam_jackhmmer"):
    os.chdir("pfam_jackhmmer")
    id=os.path.splitext(f)[0]
    input_handle = open(id+".alig", "rU")
    output_handle = open("hhalign_input/"+id+".fa", "w")

    sequences = SeqIO.parse(input_handle, "stockholm")
    count = SeqIO.write(sequences,output_handle, "fasta")
    input_handle.close()
    output_handle.close()