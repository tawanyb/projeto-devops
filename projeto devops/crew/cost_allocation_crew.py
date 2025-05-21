from crewai import Crew
from agents.data_loader_agent import DataLoaderAgent
from agents.processor_agent import ProcessorAgent
from agents.report_generator_agent import ReportGeneratorAgent

# Classe que define e executa a Crew de agentes
class CostAllocationCrew:
    def __init__(self, inputs):
        self.inputs = inputs

        # Instancia os agentes
        self.data_loader = DataLoaderAgent()
        self.processor = ProcessorAgent()
        self.reporter = ReportGeneratorAgent()

        # Cria a Crew com os três agentes
        self.crew = Crew(
            agents=[],
            process=self.run_pipeline  # Função que define a execução em sequência
        )

    def run_pipeline(self):
        # Etapa 1: carregar os dados
        data = self.data_loader.run(self.inputs)

        # Etapa 2: processar o rateio
        result = self.processor.run(data)

        # Etapa 3: gerar o relatório final
        self.reporter.run(result)

        return result

    def run(self):
        return self.crew.run()
