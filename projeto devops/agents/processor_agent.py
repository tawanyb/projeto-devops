from crewai import Agent # Import Agent direto do from crewai
import pandas as pd

# Agente responsável pelo processamento e rateio dos custos
class ProcessorAgent:
    def __init__(self):
        self.agent = Agent(name="Rateio Processor", description="Calcula o rateio proporcional")

    def run(self, data):
        df_colab = data["colaboradores"]
        df_benef = data["beneficios"]
        df_ferr = data["ferramentas"]

        # Soma dos benefícios por CPF
        benef_sum = df_benef.groupby("CPF")["Total"].sum().reset_index(name="Custo Benefício")

        # Junta as informações de colaboradores com os benefícios
        df = pd.merge(df_colab, benef_sum, on="CPF", how="left")

        # Calcula custo proporcional das ferramentas
        total_usuarios = len(df)
        total_ferr = df_ferr["Valor"].sum()
        valor_ferramenta_por_usuario = total_ferr / total_usuarios if total_usuarios else 0

        df["Custo Ferramenta"] = valor_ferramenta_por_usuario
        df["Custo Total"] = df["Custo Benefício"].fillna(0) + df["Custo Ferramenta"]

        return df