import pandas as pd
import os

    # acessa dados dos DataFrames, realiza a conversão e cria um novo DataFrame

def converter_para_hcm(df):
    df['moto_hcm'] = df['moto'] * 0.33
    df['carro_hcm'] = df['carro'] * 1.00
    df['cam_leve_hcm'] = df['cam_leve'] * 1.10
    df['cam_pesado_hcm'] = df['cam_pesado'] * 1.00
    df['especial_hcm'] = df['especial'] * 1.50
    return df


def exportar_para_excel(df, caminho_saida):
    df.to_excel(caminho_saida, index=False)


def main():
    # diretório de entrada
    diretorio_entrada = os.getcwd()

    # diretório de saída
    diretorio_saida = r'D:\Conversor_HCM\hcm_result'

    # garantir que o diretório de saída exista
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    # percorrer todos os arquivos no diretório de entrada
    for arquivo in os.listdir(diretorio_entrada):
        if arquivo.endswith('.xlsx') and arquivo.startswith('vol'):
            # ler o arquivo da planilha
            df = pd.read_excel(os.path.join(diretorio_entrada, arquivo))

            # converter os dados para o modelo HCM
            df = converter_para_hcm(df)

            nome_arquivo_saida = f'hcm_{arquivo}'
            caminho_completo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)

            # exportar para uma nova planilha
            exportar_para_excel(df, caminho_completo_saida)
            print(f'Dados convertidos foram exportados para {caminho_completo_saida}')


if __name__ == "__main__":
    main()