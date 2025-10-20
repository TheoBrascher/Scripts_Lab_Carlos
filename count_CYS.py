#!/usr/bin/python3

import re
import sys
import argparse
import os
from Bio import SeqIO

#USAGE -> ./count_CYS input_name.fasta output_name.fasta
## input_name.fasta -> nome do arquivo que queres analisar.
## output_name.fasta -> nome do arquivo que queres gerar depois da análise.


def count_cys(input_fasta, output_name):

    data = []
    for fasta in SeqIO.parse(input_fasta, "fasta"):
        seq = str(fasta.seq).upper()
        tam = len(seq)
        
        if tam == 0:
            continue

        cys = seq.count("C")
        fasta.description = fasta.description + '   ' + f'Cys count = {cys}'
        data.append(fasta)

    if data:
        SeqIO.write(data, output_name, "fasta")
            
def main():
    parser = argparse.ArgumentParser(description="Contagem do número de Cisteinas nas sequências (SERÁ INSERIDO NA DESCRIÇÃO DE CADA NOME DO FASTA)")
    parser.add_argument("input_fasta", help="Arquivo FASTA de entrada (.faa ou .fasta)")
    parser.add_argument("output_name", help="Nome do arquivo de saída com as contagens de CYS")
    args = parser.parse_args()

    count_cys(args.input_fasta, args.output_name)

if __name__ == "__main__":
    main()
