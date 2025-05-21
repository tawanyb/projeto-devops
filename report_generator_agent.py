from crewai import Agent

# Agente responsável por salvar o relatório final
class ReportGeneratorAgent:
    def __init__(self):
        self.agent = Agent(name="Relatório", description="Gera o relatório final")

    def run(self, df_resultado):
        # Salva o DataFrame em um arquivo Excel dentro da pasta outputs
        df_resultado.to_excel("outputs/relatorio_rateio.xlsx", index=False)
        print("📁 Relatório salvo em: outputs/relatorio_rateio.xlsx")
