#!/usr/bin/python3

import argparse
from Bio import SeqIO
import os


#usage ./script.py sequencias.fasta output.fasta (output.fasta -> sequências filtradas)

def filtrar_sequencias_st(input_fasta, output_fasta, limiar_percent=20):
    registros_filtrados = []

    for registro in SeqIO.parse(input_fasta, "fasta"):
        seq = str(registro.seq).upper()
        tam = len(seq)
        if tam == 0:
            continue
        s = seq.count("S")
        t = seq.count("T")
        perc = (s + t) / tam * 100
    
        if perc >= limiar_percent:
            registros_filtrados.append(registro)
    
    if registros_filtrados:
        SeqIO.write(registros_filtrados, output_fasta, "fasta")
        print(f"Salvo: {output_fasta} ({len(registros_filtrados)} seqs)")
    else:
        print(f"Nenhuma sequência passou o filtro no arquivo: {input_fasta}")

def main():
    parser = argparse.ArgumentParser(description="Filtra sequências com base na porcentagem de S/T")
    parser.add_argument("input_fasta", help="Arquivo FASTA de entrada (.faa ou .fasta)")
    parser.add_argument("output_fasta", help="Arquivo FASTA de saída")
    parser.add_argument("--limiar", type=float, default=20.0, help="Porcentagem mínima de S + T (padrão: 20.0%%)")
    args = parser.parse_args()

    filtrar_sequencias_st(args.input_fasta, args.output_fasta, args.limiar)

if __name__ == "__main__":
    main()

