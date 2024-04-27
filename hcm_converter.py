import pandas as pd
from pathlib import Path
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


# acessa dados dos DataFrames, realiza a conversão e cria novas colunas para acomodar os dados convertidos nas devidas classificações
def converter_para_hcm(df):
    df['Passeio'] = df['carro'] * 1 + df['moto'] * 0.33
    df['Pesados não articulados (SUT)'] = df['cam_leve'] * 1.1
    df['Pesados articulados (TT)'] = df['cam_pesado'] * 1 + df['especial'] * 1.5

    # adiciona uma nova linha com a soma de cada coluna e a soma total
    df.loc['Total'] = df.sum(numeric_only=True)

    # adiciona uma coluna com a soma apenas dos valores de carro, moto, cam_leve, cam_pesado e especial
    df['total_veiculos'] = df[['Passeio', 'Pesados não articulados (SUT)', 'Pesados articulados (TT)']].sum(axis=1)

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
        df['vel_media'] = df['vel_media'].astype(float)
        df['total_veiculos'] = df['total_veiculos'].astype(float)

        nome_arquivo_saida = f'hcm_{arquivo.name}'
        caminho_completo_saida = diretorio_saida / nome_arquivo_saida

        # exportar para uma nova planilha
        exportar_para_excel(df, caminho_completo_saida)
        print(f'Dados convertidos foram exportados para {caminho_completo_saida}')


if __name__ == "__main__":
    main()
