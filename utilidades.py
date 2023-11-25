import pandas as pd


class Utilidades:

    def __init__(self):
        pass

    def arruma_data(self, df):
        # Converte a coluna 'Date' para datetime e remove informações de fuso horário

        df['Date'].fillna('1500-01-01 00:00:00-03:00', inplace=True)
        df['Date'] = pd.to_datetime(df['Date']).dt.tz_convert(None)
        df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

        df['ANO'] = pd.to_datetime(df['Date']).dt.year
        df['MES'] = pd.to_datetime(df['Date']).dt.month

        return df

    def agrupamento_dividendos(self, df):

        df_dividendo = pd.DataFrame(df)

        lista_df_filtrado_ano = []

        for a in df['ANO'].unique():

            df_dividendo = df.loc[df['ANO'] == a]

            df_dividendo = df_dividendo[['TICKET', 'ANO', 'Dividends']]

            df_dividendo = df_dividendo.groupby(['TICKET', 'ANO'])['Dividends'].sum()

            lista_df_filtrado_ano.append(df_dividendo)

        df_final = pd.concat(lista_df_filtrado_ano)

        return df_final
