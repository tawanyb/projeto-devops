from crew.cost_allocation_crew import CostAllocationCrew

# Caminhos das planilhas (você pode mudar os nomes se quiser)
inputs = {
    "colaboradores": ["data/Dados Colaboradores.xlsx"],
    "beneficios": [
        "data/beneficios/Beneficio 1 - Unimed.xlsx",
        "data/beneficios/Beneficio 2 - Gympass.xlsx"
    ],
    "ferramentas": [
        "data/ferramentas/Ferramenta 1 - Github.xlsx",
        "data/ferramentas/Ferramenta 2 - Google workspace.xlsx"
    ]
}

# Executa o pipeline
crew = CostAllocationCrew(inputs)
crew.run()

print("✅ Pipeline de rateio concluído com sucesso.")
