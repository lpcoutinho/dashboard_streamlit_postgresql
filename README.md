# Análise descritiva de dados

A análise descritiva é um tipo de análise de dados que observa dados passados para descrever o que aconteceu. Os resultados geralmente são apresentados em relatórios, painéis de controle, gráficos de barras e outras visualizações de fácil compreensão.

As estatísticas descritivas fornecem resumos simples sobre a amostra e sobre as observações que foram feitas. Esses resumos podem ser tanto quantitativos, ou seja, estatísticas de resumo, quanto visuais, ou seja, gráficos simples de entender. Esses resumos podem servir como base para a descrição inicial dos dados como parte de uma análise estatística mais extensa, ou podem ser suficientes por si só para uma investigação específica.

## Etapa 01: Criando e Populando a Base de Dados

Com Beekeeper, executei o comando abaixo para criar a base de dados denominada "insurance":

```sql
create database insurance;
```

Para criar e popular a base de dados resolvi aproveitar o Python. de modo bem simples, com Pandas e SQLAlchemy crio e populo uma nova tabela no Banco de dados usando um DataFrame construido os dados contidos em *insurance.csv*

```python
df.to_sql("insurance", engine, if_exists="replace", index=True)
```

Tudo pode ser consultado em *resources/createDB.py*

## Etapa 02: Configurando a página

Configurei algumas opções gerais da página usando st.set_page_config(), como o título, um ícone e o layout(configurado como "wide" para ocupar mais espaço horizontal na tela).

Em seguida, eu inicializei uma variável theme_plotly com None, que será usada para configurar  a aparência dos gráficos Plotly.

## Etapa 03: Constuindo filtros

Depois, eu obtive dados do banco de dados chamando a função `view_all_data()` e os coloquei em um DataFrame pandas chamado df. Os nomes das colunas do DataFrame são definidos para incluir informações sobre políticas de seguros, como "Policy", "Expiry", "Location", "State", "Region", "Investment", "Construction", "BusinessType", "Earthquake", "Flood", e "Rating".

Adicionei um logotipo usando st.sidebar.image e um título "Filtre os dados". Em seguida, criei três opções de seleção múltipla para permitir ao usuário filtrar os dados com base na região, localização e tipo de construção.

## Etapa 04: Montando um menu no Sidebar

Quero criar um menu interativo que contenha duas páginas para exibir os gráficos. Para isso, crio uma função chamada sideBar, que cria um menu lateral e um superior. O menu contém duas opções principais: "Home" e "Progress". O usuário pode selecionar uma dessas opções para interagir com diferentes partes do aplicativo.

## Etapa 05: Construindo a página Home

Começo mostrando um conjunto de dados tabular com a função `st.expander` para criar uma tabela que pode ser expandida ou recolhida onde o usuário pode escolher quais colunas desejava ver usando a função `st.multiselect`.

Em seguida, calculo algumas métricas como investimento total, a moda do investimento, a média do investimento, a mediana do investimento e o risco médio. Para apresentá-las de forma clara, um layout de cinco colunas para organizar as informações.

## Etapa 06: Construindo gráficos

Em um gráfico de barras horizontais agrupo os dados por tipo de negócio (BusinessType) e conto quantos investimentos existem em cada categoria. Em seguida, classifico essas categorias com base no número de investimentos. Isso permitirá que o usuário veja facilmente em qual tipo de negócio foram feitos mais investimentos.

Crio uma segunda visualização, como um gráfico de linhas. Os dados são agrupados por estado (State) e conto quantos investimentos existem em cada estado. O gráfico de linhas permitirá ao usuário acompanhar como o número de investimentos varia de estado para estado.

Para apresentar esses gráficos, um layout de duas colunas. Isso permite que o usuário visualize ambas as visualizações lado a lado e compare os dados com facilidade.

## Etapa 07: Página de progresso

Dentro da função "progress_bar", crio uma barra de progresso para acompanhar o progresso em direção a uma meta de investimento. Adiciono um estilo CSS à barra de progresso, que permite uma transição de cores de verde para amarelo, dando um visual atraente e informativo.

Defino a meta de investimento como 3.000.000.000 (três bilhões) e calculo o valor atual do investimento somando todos os investimentos da seleção de dados. Também calculo a porcentagem de progresso em direção à meta. Isso é importante para que os usuários possam visualizar o quão perto estão de atingir a meta.

Cria a barra de progresso usando `st.progress(0)` e, em seguida, inicio um loop para atualizar a barra de progresso. Se a porcentagem ultrapassar 100%, ele exibirá a mensagem "Meta alcançada!". Caso contrário, ele mostrará o progresso atual em termos de porcentagem e valor total da meta.

Durante o loop, a barra de progresso é atualizada em incrementos, e a função "sleep(0.1)" é usada para criar uma animação suave do progresso. Isso ajuda os usuários a acompanhar o progresso de forma visual.

Além da barra de progresso, adiciono e edito um gráfico de pizza que exibe as classificações por estado com `st.plotly_chart`.

![1](resources/img/dash_01.png)
![1](resources/img/dash_02.png)
![1](resources/img/dash_03.png)