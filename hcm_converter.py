import pandas as pd
from pathlib import Path
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


# acessa dados dos DataFrames, realiza a conversão e substitui os valores das colunas existentes
def converter_para_hcm(df):
    df['moto'] = df['moto'] * 0.33
    df['carro'] = df['carro'] * 1.00
    df['cam_leve'] = df['cam_leve'] * 1.10
    df['cam_pesado'] = df['cam_pesado'] * 1.00
    df['especial'] = df['especial'] * 1.50

    # adiciona uma nova linha com a soma de cada coluna e a soma total
    df.loc['Total'] = df.sum(numeric_only=True)

    # adiciona uma coluna com a soma apenas dos valores de carro, moto, cam_leve, cam_pesado e especial
    df['total_veiculos'] = df[['moto', 'carro', 'cam_leve', 'cam_pesado', 'especial']].sum(axis=1)

    return df


def exportar_para_excel(df, caminho_saida):
    df.to_excel(caminho_saida, index=True)


def main():
    # diretório de entrada
    diretorio_entrada = Path.cwd()

    # diretório de saída
    diretorio_saida = Path(r'D:\Conversor_HCM\hcm_result')

    # garantir que o diretório de saída exista
    diretorio_saida.mkdir(parents=True, exist_ok=True)

    # percorrer todos os arquivos no diretório de entrada
    for arquivo in diretorio_entrada.glob('vol*.xlsx'):
        # ler o arquivo da planilha
        df = pd.read_excel(arquivo)

        # converter os dados para o modelo HCM
        df = converter_para_hcm(df)

        nome_arquivo_saida = f'hcm_{arquivo.name}'
        caminho_completo_saida = diretorio_saida / nome_arquivo_saida

        # exportar para uma nova planilha
        exportar_para_excel(df, caminho_completo_saida)
        print(f'Dados convertidos foram exportados para {caminho_completo_saida}')


if __name__ == "__main__":
    main()