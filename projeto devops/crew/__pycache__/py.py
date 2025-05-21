%%writefile agents/data_loader_agent.py
import pandas as pd
from crewai.agents import Agent

# Agente responsável por carregar e limpar os dados das planilhas
class DataLoaderAgent:
    def __init__(self):
        pass  # Nenhuma instância de Agent é necessária aqui

    def _padroniza_cpf(self, df):
        if "CPF" in df.columns:
            df["CPF"] = df["CPF"].astype(str).str.replace(r'\D', '', regex=True)
        return df

    def _carrega_multiplos(self, arquivos, tipo, required_cols):
        if not isinstance(arquivos, list):
            arquivos = [arquivos]

        dataframes = []

        for caminho in arquivos:
            try:
                df = pd.read_excel(caminho)
                df.columns = [c.strip() for c in df.columns]

                if not all(c in df.columns for c in required_cols):
                    print(f"Skipping {caminho} due to missing required columns: {required_cols}")
                    continue

                df = self._padroniza_cpf(df)

                if tipo == "beneficios":
                    if "Tipo" in df.columns:
                        df = df[df["Tipo"].astype(str).str.upper() == "T"]
                    else:
                        print(f"Warning: 'Tipo' column not found in {caminho}. Skipping filtering.")

                dataframes.append(df)

            except FileNotFoundError:
                print(f"Erro: Arquivo não encontrado em {caminho}")
            except Exception as e:
                print(f"Erro carregando {caminho}: {e}")

        return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

    def run(self, inputs):
        colab_input = inputs.get("colaboradores", [])
        benef_input = inputs.get("beneficios", [])
        ferr_input = inputs.get("ferramentas", [])

        if isinstance(colab_input, str):
            colab_input = [colab_input]
        elif not isinstance(colab_input, list):
            colab_input = []

        return {
            "colaboradores": self._carrega_multiplos(colab_input, "colaboradores", ["CPF"]),
            "beneficios": self._carrega_multiplos(benef_input, "beneficios", ["CPF", "Total", "Tipo"]),
            "ferramentas": self._carrega_multiplos(ferr_input, "ferramentas", ["Valor"])
        }
