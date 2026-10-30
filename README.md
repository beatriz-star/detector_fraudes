1 - Sobre o projeto: 
O FraudLens consiste em um projeto acadêmico, desenvolvido em Python, cujo objetivo é investigar características e padrões presentes em transações financeiras legítimas e fraudulentas. 
É utilizada uma base de dados pública de transações com cartões de crédito, e o projeto apresenta os resultados por meio de um dashboard interativo, desenvolvido com Streamlit. Através dele, exploramos dados, comparamos categorias de transações e visualizamos relações entre variáveis relevantes para a análise de transações fraudulentas. 
O foco do projeto é transformar dados em informações compreensíveis por meio de visualizações e estatísticas descritivas. 
2 - Objetivos:
Explorar e compreender uma base de dados de transações financeiras. 
Comparar transações legítimas e fraudulentas.
Analisar a distribuição dos valores das transações. 
Investigar a distribuição temporal aproximada das fraudes. 
Visualizar correlações entre as variáveis numéricas. 
Desenvolver um dashboard interativo para facilitar a exploração dos dados. 
3 - Base de dados:
O projeto utiliza a base Credit Card Fraud Detection, disponibilizada no Kaggle. 
A base original contém 283.726 transações, das quais 493 são classificadas como fraudes. A base possui 31 colunas, incluindo:
Time: tratando do tempo decorrido, em segundos, desde a primeira transação registrada. 
Amount: valor monetário da transação. 
V1 a V28: variáveis numéricas transformadas e anonimizadas. 
Class: classificação da transação, em que 0 representa uma transação legítima e 1 representa uma fraude. 
O processamento inclui o tratamento de registros sem classificação válida, a remoção de classificações fora das categorias esperadas e remoção de quaisquer registros duplicados. 
Fonte dos dados: Credit Card Fraud Detection - Kaggle
4 - Tecnologias e bibliotecas utilizadas:
Python: Linguagem utilizada no desenvolvimento do projeto. 
Pandas: Leitura, limpeza, organização, filtragem e análise de dados. 
NumPy: Suporte a operações numéricas e manipulação de dados. 
Matplotlib: Construção e personalização de gráficos. 
Seaborn: Criação de visualizações estatísticas. Incluindo box plot e mapas de calor. 
Streamlit: Desenvolvimento da interface interativa do dashboard. 
Pathlib: Organização e gerenciamento de caminhos de arquivos. 
Visual Studio Code: Desenvolvimento das análises e espaço de desenvolvimento do projeto. 
5 - Funcionalidades do dashboard:
O FraudLens apresenta indicadores e visualizações que permitem explorar os dados de maneira interativa. 
Indicadores gerais: O dashboard aborda o total de transações da base tratada, a quantidade de transações no resultado filtrado, o número de fraudes identificadas, a taxa de fraude no resultado e o valor monetário associado às transações fraudulentas selecionadas. 
Filtros interativos: Os filtros permitem selecionar tanto os tipos de transação quanto definir um valor máximo para as operações analisadas. Os indicadores e visualizações que dependem dos filtros são atualizados de acordo com a seleção. 
Visualizações: O projeto aborda 5 tipos de gráficos, que apesar de abordarem os mesmos dados, os apresentam de formas diferentes para diferentes tipos de interpretações visuais. 
Distribuição das transações: compara a quantidade de transações legítimas e fraudulentas. 
Boxplot dos valores: compara a mediana, a dispersão e os possíveis valores atípicos das transações de cada categoria. 
Distribuição temporal aproximada das fraudes: apresenta a quantidade de fraudes ao longo de um ciclo de 24 horas derivado da variável Time. É importante frisar que neste gráfico, os horários não são exatos, e sim aproximados. 
Mapa de calor das correlações: explora as relações lineares entre as variáveis numéricas e a classificação das transações. 
Resumo estatístico: apresenta medidas descritivas dos valores das transações, como: contagem, média, mediana, desvio-padrão, mínimo e máximo. O resumo apoia a interpretação e leitura do boxplot. 
6 - Principais conclusões:
Desequilíbrio entre as classes: a quantidade de transações legítimas é exponencialmente superior à de transações fraudulentas, uma diferença que precisa ser considerada na interpretação dos resultados e em possíveis estudos futuros de detecção de fraudes.
Comparação dos valores: a análise dos valores permite investigar diferenças entre transações legítimas e fraudulentas, incluindo medidas de tendência central e dispersão. 
Distribuição temporal: a visualização temporal aproximada nos permite explorar possíveis concentrações de fraudes em determinados intervalos do ciclo construído a partir da variável Time. Essa análise não representa necessariamente os horários reais do dia, mas uma aproximação que possibilita uma estimativa. 
Relações entre variáveis: o heatmap nos permite identificar associações lineares entre variáveis numéricas e a classificação das transações, contribuindo para a formulação de hipóteses para análises futuras. 
Importância da análise exploratória:  os gráficos e estatísticas descritivas facilitam a identificação e interpretação de características relevantes, ajudando a orientar investigações posteriores. 
7 - Limitações do projeto:
O FraudLens é uma ferramenta exploratória, não um modelo preditivo de detecção de fraudes.
O dashboard utiliza as classificações que já estavam presentes na base de dados, sem capacidade de prever se uma nova transação seria fraudulenta. Além disso, por questões de privacidade e segurança, as variáveis são anonimizadas, limitando a interpretação em termos de características financeiras. 
A distribuição temporal (o 2º tópico) também exige cautela e interpretação cuidadosa, uma vez que a variável Time representa o tempo decorrido desde a primeira transação registrada, não um horário real. 
8 - Considerações finais:
O FraudLens demonstra a aplicação de Python e de bibliotecas utilizadas na análise de dados, utilizadas no contexto da exploração de transações financeiras.

Ele reúne preparação de dados, estatística descritiva, visualização e desenvolvimento de uma interface interativa, contribuindo para a compreensão dos dados e para a construção de uma base para estudos futuros sobre detecção de fraudes. 
