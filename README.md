# PROTOCOLO PARA USO DOS SCRITPS
Scripts para análise e filtragem de sequências proteicas

## 1. Rodar o script filtrar_ST20.py
### 🧩 Função
- Este script irá contar o número de Serinas e Treoninas de cada sequência fasta. 
- Após a contagem, o script irá verificar a porcentagem (limiar) de Serina+Treonia em relação a sequência toda.
 	Caso der uma porcentagem maior que o limiar (20%), ela irá selecionar essa sequência para ser salva.
	Caso não respeitar essa porcentagem, a sequência é descartada.
	Como resultado, apenas as sequências com a quantidade de Serina+Treonia que forem maior ou igual a 20% serão salvas.

### ⚙️ Como rodar o script
	./filtrar_ST20.py input_name.fasta output_name.fasta 
Parâmetros obrigatórios:
- input_name.fasta -> nome do arquvio para ser analisado
  
- output_name.fasta -> nome do arquivo que será gerado com as sequências filtradas

### 🧠 Opções de modificação
--limiar LIMIAR  Porcentagem mínima de S + T (padrão: 20.0%)
	Pode alterar o limiar com a flag --limiar
	Exemplo: ./filtrar_ST20.py input_name.fasta output_name.fasta --limar 35
		Nesse caso, serão filtradas as sequências com a quantidade de Serina+Treonia que forem maior ou igual a 35%.


## 2. Rodar o script filtrar_PTS.py
### 🧩 Função
- Este script irá contar a quantidade de motivos PTS de cada sequência fasta.
- A quantidade será anotada na descrição da sequência FASTA
	Ex: 
	Antes:  >SEQ012871
	Depois: >SEQ012871 Número de motivos PTS = 5

- Após a contagem, o script irá verificar se a sequência possui um numéro de motivo PTS igual ou maior que 3 (limiar).
	Caso positivo, ela irá selecionar essa sequência para ser salva.
	Caso negativo, ela será descartada.
	Como resultado, serão salvas as sequências que apresentarem um numéro de motivo PTS igual ou maior que 3.

### ⚙️ Como rodar o script
	./filtrar_PTS.py input_name.fasta output_name.fasta 
Parâmetros obrigatórios:
- input_name.fasta -> nome do arquvio para ser analisado
  
- output_name.fasta -> nome do arquivo que será gerado com as sequências filtradas

### 🧠 Opções de modificação
--limiar LIMIAR  Quantidade de motivos PTS mínimo para filtar as sequências
        Pode alterar o limiar com a flag --limiar
        Exemplo: ./filtrar_PTS.py input_name.fasta output_name.fasta --limar 10
                Nesse caso, serão filtradas as sequências que apresentarem um numéro de motivo PTS igual ou maior que 20.


##  3. Submeter as sequências no programa NetOGlyc - 4.0
### 🧩 site -> https://services.healthtech.dtu.dk/services/NetOGlyc-4.0/

- O arquivo contendo as sequêncais filtradas deverão passar pelo programa NetOGlyc para analisar as glicosilações das sequências.
	Aqui é indicado o parcionamento das sequências pois o programa tem um limite de tempo. Se rodar muitas sequências, é muito provável que a análise irá superar o limite de tempo, não gerando output.
		Recomendável: 20-30 sequêncais por análise.

- Deve salvar o resultado final do NetOGlyc em um arquivo de texto txt (Ex: Mucin_1_gff.txt)
	❗❗ Cuidar para que as mesmas sequências fasta tenham o mesmo nome do arquivo txt que será gerado com as informações do NetOGlyc ❗❗
	Ex: Mucin_1.fasta -> nome do arquivo de entrada para NetOGlyc
	    Mucin_1_gff.txt -> nome do arquivo que será salvo as informações resultantes do NetOGlyc

	Esse cuidado é importante pois no próximo passo será utilizado esses pares de arquivos!

### 🧠 Dica
- Pode utilizar o script get_fasta_split.py para parcionar o arquivo fasta.
	🧩 Esse script irá dividir o arquivo fasta em outros arquivos contando 30 sequências cada (limiar)

### ⚙️ Como rodar o script
	/get_fasta_split.py input_name.fasta output_name
Parâmetros obrigatórios:
- input_name.fasta -> nome do arquvio para ser analisado

- output_name -> ATENÇÃO!! aqui é somente um nome para o script usar de referência.
	Ex.: Mucins_test
	Reultado esperado, Mucins_test_1, Mucins_test_2, Mucins_test_3 ...	
	
### 🧠 Opções de modificação
--limiar LIMIAR  altera a quantidade de sequências por arquivo. 
        Pode alterar o limiar com a flag --limiar
        Exemplo: ./ get_fasta_split.py input_name.fasta output_nam --limar 100 
                Nesse caso, serão gerados arquivos contendo 100 sequências cada.


## 4. Rodar o script filtrar_OG20.py
### 🧩 Função
- Este script contar a quantidade de sítios de glicosição das sequências. 
- Após a contagem, o script irá verificar se a sequência possui 20% de sítios POSITIVES para glicosilações preditas pelo programa NetOGlyc.
        Caso positivo, ela irá selecionar essa sequência para ser salva.
        Caso negativo, ela será descartada.

### ⚙️ Como rodar o script
	./filtrar_OG20.py --fasta input_name.fasta --gff input_gff.txt --saida output_name.fasta
Parâmetros obrigatórios:
--fasta input_name.fasta -> nome do arquvio para ser analisado

--gff input_gff.txt -> nome do arquivo txt que foi salvo com as informações do NetOGlyc ❗

--saida output_name.fasta -> nome do arquivo que será gerado com as sequências filtradas


## 5. Rodar o script count_CYS.py
### 🧩 Função
- Este script irá contar a quantidade de Cisteínas presente na sequência e deixar anotada em sua descrição.
       Ex:
        Antes:  >SEQ012871
        Depois: >SEQ012871 Número de motivos Cys = 50

Como será contada também o PTS em scripts anteriores, é provável que fique assim:
	Depois: >SEQ012871 Número de motivos PTS = 5 Número de motivos Cys = 50

### ⚙️ Como rodar o script
	./count_CYS.py input_name.fasta output_name.fasta
Parâmetros obrigatórios:
- input_name.fasta -> nome do arquivo que queres analisar.

- output_name.fasta -> nome do arquivo que queres gerar depois da análise.


## 6. Rodar as sequências filtradas no Interproscan e anotar a descrição de cada uma.
### 🧩 Site -> https://www.ebi.ac.uk/interpro/search/sequence/



