# Análise do desempenho escolar de estudantes

## Integrante
- **Nome:** Ana de Kassia da Silva Soares

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
O arquivo original foi mantido sem alterações. Para realizar a análise, utilizou-se uma cópia dos dados, na qual foram feitas verificações de valores ausentes, registros duplicados, tipos de informações e possíveis valores fora do esperado. Em cada análise, foram consideradas apenas os dados válidos para as variáveis utilizadas.

## Principais conclusões
**A análise dos dados de 649 estudantes permitiu identificar relações entre hábitos de estudo, frequência escolar e desempenho acadêmico.

Os resultados indicaram que os estudantes que dedicam mais horas aos estudos tendem a apresentar notas finais mais elevadas, principalmente no grupo que estuda de 5 a 10 horas por semana.

Também foi identificada uma correlação negativa fraca entre o número de faltas e a nota final (Spearman = -0,159; p = 0,00005), indicando que o aumento das ausências está associado a uma pequena redução no desempenho.

Na comparação entre os sexos, foi observada diferença estatisticamente significativa nas notas finais (Mann-Whitney; p = 0,000632), com média de 12,25 para o grupo feminino e 11,41 para o masculino.

Conclui-se que a gestão escolar pode utilizar esses resultados para incentivar hábitos de estudo, acompanhar a frequência dos alunos e identificar dificuldades de aprendizagem, desenvolvendo ações que contribuam para melhorar o desempenho escolar e garantir oportunidades iguais para todos.

## Teste de hipótese
- H₀: não há diferença entre os grupos comparados.
- H₁: há diferença entre os grupos.
- Nível de significância: 5% (α = 0,05).
- O notebook seleciona o teste t de Welch ou Mann–Whitney conforme o diagnóstico de normalidade e imprime o valor-p e a decisão estatística.

