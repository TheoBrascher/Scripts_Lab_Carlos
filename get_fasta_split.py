#!/usr/bin/python3

import sys
import argparse
import os
from Bio import SeqIO

#USAGE -> ./count_CYS input_name.fasta output_name.fasta
## input_name.fasta -> nome do arquivo que queres analisar.
## output_name.fasta -> nome do arquivo que queres gerar depois da análise.


def get_fasta_split(input_fasta, output_name, limiar):

    data = []
    for fasta in SeqIO.parse(input_fasta, "fasta"):
        data.append(fasta)

    n_divisions = len(data)//limiar
    n_lists = len(data)//n_divisions
    last = max(range(n_divisions))

    for i in range(n_divisions):
        start = i * n_lists
    
        if i == last:
            final = -1
        else:
            final = start + n_lists

        SeqIO.write(data[start:final], f'{output_name}_{i}.fasta', "fasta")
    
            
def main():
    parser = argparse.ArgumentParser(description="Particionamento de sequêncais de arquivos fasta")
    parser.add_argument("input_fasta", help="Arquivo FASTA de entrada (.faa ou .fasta)")
    parser.add_argument("output_name", help="Nome do arquivo de saída")
    parser.add_argument("--limiar", type=float, default=30, help="Quantidade de sequências por arquivo")
    args = parser.parse_args()

    get_fasta_split(args.input_fasta, args.output_name, args.limiar)

if __name__ == "__main__":
    main()
