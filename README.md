# Projeto Agente de IA para Rateio de Custos

## Descrição

Este projeto implementa um agente de IA utilizando o framework **CrewAI** para orquestrar o processo de rateio de custos em uma empresa. O agente recebe como entrada planilhas contendo informações sobre colaboradores, ferramentas (softwares) e benefícios, realiza o processamento e cálculo dos custos alocados por colaborador e gera um relatório consolidado em formato Excel, além de uma visualização gráfica.

## Funcionalidades

- Leitura e padronização de múltiplas planilhas (.xlsx)
- Cálculo do custo de ferramentas e benefícios por colaborador
- Agregação e somatório dos custos totais
- Geração de relatório Excel final consolidado
- Visualização gráfica dos custos por colaborador (gráfico de barras)

## Tecnologias Utilizadas

- Python 3.8+
- [CrewAI](https://github.com/crewai/crewai) para orquestração de agentes de IA
- OpenAI GPT (via LangChain/OpenAI API) para suporte ao agente
- Pandas para manipulação de dados
- Matplotlib para visualização gráfica

## Estrutura do Projeto

├── agents/                          ← Códigos dos agentes CrewAI
│   ├── __init__.py
│   ├── data_loader_agent.py         ← Agente que carrega os dados
│   ├── processor_agent.py           ← Agente que processa o rateio
│   └── report_generator_agent.py    ← Agente que gera o relatório
│
├── crew/
│   └── cost_allocation_crew.py      ← Classe que monta e executa a Crew
│
├── data/                            ← PLANILHAS DE ENTRADA VÃO AQUI
│   ├── Dados Colaboradores.xlsx
│   ├── Beneficio 1 - Unimed.xlsx
│   ├── Beneficio 2 - Gympass.xlsx
│   ├── Ferramenta 1 - Github.xlsx
│   └── Ferramenta 2 - Google workspace.xlsx
│
├── outputs/                         ← SAÍDA DO RELATÓRIO FINAL
│   └── (será criado: relatorio_rateio.xlsx)
│
├── main.py                          ← Arquivo principal que executa o pipeline
└── requirements.txt                 ← Dependências do projeto
