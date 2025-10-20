#!/usr/bin/python3

import re
import sys
import argparse
import os
from Bio import SeqIO



def generate_combinations():
    amoni_acids = ['P', 'T', 'S']
    
    preliminar_data = []
    for pos1 in amoni_acids:
        for pos2 in amoni_acids:
            for pos3 in amoni_acids:
                for pos4 in amoni_acids:
                    for pos5 in amoni_acids:
                        for pos6 in amoni_acids:
                            sequence = f"{pos1}{pos2}{pos3}{pos4}{pos5}{pos6}"
                            preliminar_data.append(sequence)

    final_data = []
    for seq in preliminar_data:
        if seq in final_data:
            continue
        else:
            final_data.append(seq)

    return final_data

def filter_PTS_sequences(input_fasta, output_fasta, limiar):

    pts_sequences = generate_combinations()
    filtered_sequences  = []

    for fasta in SeqIO.parse(input_fasta, "fasta"):

        seq = str(fasta.seq).upper()
        tam = len(seq)
        if tam == 0:
            continue

        motifs_found = 0
        for pts in pts_sequences:
            matches = [match.start() for match in re.finditer(pts, seq)]
            found = len(matches)
            motifs_found += found

        if motifs_found >= limiar:
            filtered_seqences.description += '  ' + 'Número de motivos PTS = {found}' + ' '
            filtered_sequences.append(fasta)

    if filtered_sequences:
        SeqIO.write(filtered_sequences, output_fasta, "fasta")
            
def main():
    parser = argparse.ArgumentParser(description="Filtra sequências que possuem 3 ou mais motivos PTS")
    parser.add_argument("input_fasta", help="Arquivo FASTA de entrada (.faa ou .fasta)")
    parser.add_argument("output_fasta", help="Arquivo FASTA de saída")
    parser.add_argument("--limiar", type=float, default=3, help="Quantidade de motivos PTS mínimo para filtar as sequências")
    args = parser.parse_args()

    filter_PTS_sequences(args.input_fasta, args.output_fasta, args.limiar)

if __name__ == "__main__":
    main()
