from crewai import Crew, Agent # Import Agent directly from crewai
import pandas as pd

# Agente responsável por carregar e limpar os dados das planilhas
class DataLoaderAgent:
    def __init__(self):
        self.agent = Agent(name="Data Loader", description="Carrega e prepara os dados")

    def _padroniza_cpf(self, df):
        # Remove caracteres especiais do CPF
        if "CPF" in df.columns:
            df["CPF"] = df["CPF"].astype(str).str.replace(r'\D', '', regex=True)
        return df

    def _carrega_multiplos(self, arquivos, tipo, required_cols):
        # Garante que seja uma lista de arquivos
        if not isinstance(arquivos, list):
            arquivos = [arquivos]

        dataframes = []

        for caminho in arquivos:
            try:
                df = pd.read_excel(caminho)  # Lê a planilha
                df.columns = [c.strip() for c in df.columns]  # Remove espaços extras

                # Verifica se as colunas obrigatórias existem
                if not all(c in df.columns for c in required_cols):
                    continue

                df = self._padroniza_cpf(df)

                # Filtra apenas titulares em benefícios
                if tipo == "beneficios":
                    df = df[df["Tipo"].str.upper() == "T"]

                dataframes.append(df)
            except Exception as e:
                print(f"Erro carregando {caminho}: {e}")

        # Retorna DataFrame combinado
        return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

    def run(self, inputs):
        return {
            "colaboradores": self._carrega_multiplos(inputs["colaboradores"], "colaboradores", ["CPF"]),
            "beneficios": self._carrega_multiplos(inputs["beneficios"], "beneficios", ["CPF", "Total", "Tipo"]),
            "ferramentas": self._carrega_multiplos(inputs["ferramentas"], "ferramentas", ["Valor"])
        }