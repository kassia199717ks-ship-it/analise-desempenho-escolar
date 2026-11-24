# Análise do desempenho escolar de estudantes

## Integrante
- **Nome:** [preencha com seu nome]

## Objetivo
Investigar fatores associados às notas finais de estudantes de Língua Portuguesa, utilizando dados públicos do UCI Machine Learning Repository.

## Base de dados
**Student Performance — Portuguese language (`student-por.csv`)**. A base original contém 649 registros e 33 variáveis, coletados em duas escolas secundárias de Portugal.

Fonte: [UCI Machine Learning Repository — Student Performance](https://archive.ics.uci.edu/dataset/320/student%2Bperformance)  
DOI: https://doi.org/10.24432/C5TG7T

## Perguntas investigadas
1. Alunos que estudam mais horas por semana apresentam notas finais maiores?
2. O número de faltas está relacionado à nota final?
3. Existe diferença estatisticamente significativa entre as notas finais de estudantes do sexo feminino e masculino?

## Estrutura
```text
projeto-desempenho-escolar/
├── dados/
│   └── student-por.csv       # base original, sem alterações
├── analise_desempenho.ipynb  # notebook comentado
└── README.md
```

## Como executar
1. Coloque o arquivo original `student-por.csv` dentro da pasta `dados/`.
2. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy jupyter
   ```
3. Abra o notebook:
   ```bash
   jupyter notebook analise_desempenho.ipynb
   ```
4. No Jupyter, selecione **Kernel > Restart & Run All** (ou **Reiniciar e executar tudo**).

O notebook lê a base com caminho relativo: `pd.read_csv('dados/student-por.csv', sep=';')`.

## Preparação dos dados
O arquivo original é preservado. O notebook cria uma cópia em memória para conferir valores ausentes, duplicatas, tipos e faixas. Para cada análise, utiliza apenas os registros com valores válidos nas variáveis envolvidas.

## Principais conclusões
**Preencher após executar o notebook.** Registrar aqui os resultados reais das três análises, incluindo o teste escolhido e o valor-p. Não inserir conclusões antes de conferir a saída do notebook.

## Teste de hipótese
- H₀: não há diferença entre os grupos comparados.
- H₁: há diferença entre os grupos.
- Nível de significância: 5% (α = 0,05).
- O notebook seleciona o teste t de Welch ou Mann–Whitney conforme o diagnóstico de normalidade e imprime o valor-p e a decisão estatística.

## Reflexão
O projeto foi desenvolvido individualmente. A mesma pessoa realizou a escolha da base, preparação, análise, visualizações, interpretação e documentação. Completar a reflexão sobre o que foi mais simples em Python do que em planilhas após realizar a atividade.

## Limitações
Os dados descrevem estudantes de duas escolas de Portugal. Associação estatística não comprova causalidade e os resultados não devem ser generalizados automaticamente para outras populações.
