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
