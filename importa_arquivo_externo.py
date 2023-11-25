import pandas as pd
import path_arquivos


class Importa_arquivo_externo:

    def __init__(self):
        pass

    def importa_lista_tickets(self):
        p = path_arquivos.Path_arquivos()

        df_tickets = pd.read_excel(p.lista_tickets)

        return df_tickets
