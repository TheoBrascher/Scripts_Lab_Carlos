#!/usr/bin/python3


import argparse
from collections import defaultdict
from Bio import SeqIO

def contar_sites_glicosilados(gff_path):
    positivos = defaultdict(list)
    with open(gff_path) as gff:
        for linha in gff:
            if linha.strip() == "" or linha.startswith("#"):
                continue
            colunas = linha.strip().split("\t")
            if len(colunas) >= 9 and "#POSITIVE" in colunas[-1]:
                seq_id = '.'.join(colunas[0].rsplit('_', 1))
                pos = int(colunas[3])
                positivos[seq_id].append(pos)
    return positivos

def calcular_percentuais(fasta_path, gff_path, saida_fasta, limiar=20.0):
    registros = SeqIO.to_dict(SeqIO.parse(fasta_path, "fasta"))
    positivos = contar_sites_glicosilados(gff_path)
    
    selecionadas = []

    print("\nID\tTamanho\t#POSITIVES\t% Glicosiladas")
    for seq_id, seq in registros.items():
        tam = len(seq.seq)
        n_pos = len(positivos.get(seq_id, []))
        perc = (n_pos / tam * 100) if tam > 0 else 0
        print(f"{seq_id}\t{tam}\t{n_pos}\t\t{perc:.2f}%")

        if perc >= limiar:
            selecionadas.append(seq)

    if selecionadas:
        SeqIO.write(selecionadas, saida_fasta, "fasta")
        print(f"\n{len(selecionadas)} sequência(s) com ≥ {limiar:.1f}% de sítios #POSITIVE salvas em '{saida_fasta}'")
    else:
        print(f"\nNenhuma sequência com ≥ {limiar:.1f}% de sítios #POSITIVE encontrada.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filtra sequências com ≥ 20%% de sítios #POSITIVE e imprime percentuais de todas.")
    parser.add_argument("--gff", required=True, help="Arquivo de entrada em formato GFF")
    parser.add_argument("--fasta", required=True, help="Arquivo FASTA com as sequências")
    parser.add_argument("--saida", required=True, help="Arquivo FASTA de saída com sequências selecionadas")
    
    args = parser.parse_args()
    calcular_percentuais(args.fasta, args.gff, args.saida, limiar=20.0)
