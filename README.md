Conversor de dados para o modelo HCM

Este script python foi desenvolvido para converter dados de veículos de uma planilha excel para o Modelo de Capacidade de Carga de Rodovias (HCM - Highway Capacity Manual) afim de facilitar a execução do trabalho 1 da disciplina Engenharia de Tráfego da Universidade Federal de Santa Catarina. O HCM é uma referência amplamente utilizada para análise de desempenho de transporte rodoviário.

Este script proporciona uma maneira eficiente de converter dados de veículos em um formato compatível com o modelo HCM, facilitando assim a análise de capacidade e desempenho de transporte rodoviário.

1 - Funções: 

* converter_para_hcm(df):

- Esta função recebe um DataFrame pandas contendo dados de veículos e realiza a conversão desses dados para o modelo HCM.
- Os parâmetros de conversão são aplicados aos diferentes tipos de veículos (moto, carro, caminhão leve, caminhão pesado, veículos especiais) e são multiplicados por fatores específicos para obter as capacidades de carga equivalente.

* exportar_para_excel(df, caminho_saida):

- Esta função exporta o DataFrame pandas convertido para um arquivo Excel.
- Recebe como entrada o DataFrame convertido e o caminho de saída para o arquivo Excel.

main():

- Função principal que gerencia o fluxo de execução do script.
- Define os diretórios de entrada e saída.
- Percorre todos os arquivos no diretório de entrada que têm extensão .xlsx e começam com o prefixo 'vol'.
-Para cada arquivo encontrado, lê o conteúdo da planilha Excel, converte os dados para o modelo HCM, exporta o DataFrame convertido para um novo arquivo Excel no diretório de saída e imprime uma mensagem indicando o sucesso da conversão e exportação.

2 - Utilização do script: 

Para executar o script, basta executar o arquivo Python conversor_hcm.py no terminal ou em um ambiente Python. Certifique-se de que as planilhas a serem analisadas e convertidas pelo script estejam no mesmo diretório do script e que tenha uma pasta com o nome hcm_result para que a conversão seja exportada para o diretório definido no script.

Autor:

Esse script foi desenvolvido por Willian Gomes de Oliveira, graduando em Engenharia Civil na Universidade Federal de Santa Catarina. 

Última atualização: 

19/03/2024
