import yfinance as yf
import pandas as pd
import utilidades
import importa_arquivo_externo
from datetime import datetime


class Request_dados:

    def __init__(self):
        pass

    def procura_dados(self):
        u = utilidades.Utilidades()

        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%Y-%m-%d")

        simbolo_acao = "BBAS3.SA"
        data_inicio = data_formatada
        data_fim = data_formatada

        dados_acao = yf.download(simbolo_acao, start=data_inicio, end=data_fim)

        df = pd.DataFrame(dados_acao)

        df['TICKET'] = simbolo_acao

        writer = pd.ExcelWriter('C:/Users/paulo/Downloads/ACOES/RESULTADO.xlsx')

        df.to_excel(writer, sheet_name=simbolo_acao, engine='xlsxwriter')

        writer.close()

    def procura_dividendos(self):
        u = utilidades.Utilidades()
        importar = importa_arquivo_externo.Importa_arquivo_externo()

        lista_dividendos = []

        df_tickets = importar.importa_lista_tickets()

        qtde_tickets = len(df_tickets)

        for i in range(qtde_tickets):

            ticket_atual = df_tickets.loc[i, 'TICKET_CONVERTIDO']

            print('Buscando historico de dividendos: ' + ticket_atual)

            try:

                ticket = yf.ticker.Ticker(ticket_atual)

                dy = ticket.dividends
                df_dy = pd.DataFrame(dy)
                df_dy = df_dy.reset_index()
                df_dy['TICKET'] = ticket_atual

                df_dy = u.arruma_data(df_dy)

                lista_dividendos.append(df_dy)

            except Exception as e:

                # Se ocorrer qualquer outro tipo de erro, imprime o aviso e o tipo de erro

                print(f"Erro ao baixar dados para ")

        df_dividendos_final = pd.concat(lista_dividendos)

        df_dividendos_resumo_ano = u.agrupamento_dividendos(df_dividendos_final)

        writer = pd.ExcelWriter('C:/Users/paulo/Downloads/ACOES/RESULTADO-DY.xlsx')

        df_dividendos_final.to_excel(writer, sheet_name='DIVIDENDOS-GERAL' + '-DY', engine='xlsxwriter')
        df_dividendos_resumo_ano.to_excel(writer, sheet_name='DIVIDENDOS-RESUMO' + '-DY', engine='xlsxwriter')

        writer.close()


r = Request_dados()

r.procura_dados()
r.procura_dividendos()
