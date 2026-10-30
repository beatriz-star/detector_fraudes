from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Análise de Fraudes",
    page_icon="🔎",
    layout="wide"
)

sns.set_theme(
    style="whitegrid",
    rc={
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",
        "axes.edgecolor": "#B0B0B0",
        "axes.labelcolor": "#404040",
        "text.color": "#262626",
        "xtick.color": "#404040",
        "ytick.color": "#404040",
        "grid.color": "#D9D9D9",
        "grid.alpha": 0.6,
    }
)
st.title("🔎 FraudLens")
st.subheader("Análise de fraudes em transações financeiras")
st.caption(
    "Base pública de transações com cartões de crédito."
)
CAMINHO = Path(
    r"C:\Users\Vaio\OneDrive\Documentos\detector_fraudes\data\creditcard.csv"
)


@st.cache_data
def carregar_dados(caminho):

    dados = pd.read_csv(caminho)
    dados = dados.dropna(subset=["Class"]).copy()
    dados = dados[dados["Class"].isin([0, 1])].copy()

    dados = dados.drop_duplicates().copy()
    dados["Tipo"] = dados["Class"].map({
        0: "Legítima",
        1: "Fraude"
    })

    dados["Hora_aproximada"] = (
        (dados["Time"] // 3600) % 24
    ).astype(int)

    return dados

if not CAMINHO.exists():
    st.error(
        "Arquivo não encontrado. Baixe creditcard.csv"
        "e coloque-o na pasta detector_fraudes"
    )
    st.stop()

df= carregar_dados(str(CAMINHO))
st.sidebar.header("Filtros")
total_base = len(df)
tipos_disponiveis = ["Legítima", "Fraude"]
tipos = st.sidebar.multiselect(
    "Tipos de transação",
    options=tipos_disponiveis,
    default=tipos_disponiveis
)
valor_maximo = float(df["Amount"].max())
limite = st.sidebar.slider(
    "Valor máximo da transação",
    min_value=0.0,
    max_value=max(valor_maximo, 1.0),
    value=max(valor_maximo, 1.0)
)
filtrado = df[
    df["Tipo"].isin(tipos)
    & (df["Amount"] <= limite)
].copy()
total_filtrado = len(filtrado)
fraudes = int((filtrado["Class"] == 1).sum())
taxa = (
    fraudes / total_filtrado * 100
    if total_filtrado > 0 
    else 0.0
)
valor_fraudes = filtrado.loc[
    filtrado["Class"] == 1, "Amount"
].sum()
filtros_ativos = []
if set(tipos) != set(tipos_disponiveis):
    if tipos:
        filtros_ativos.append(
            "Tipo: " + ", ".join(tipos)
        )
    else:
        filtros_ativos.append("Tipo: nenhum selecionado")
if limite < valor_maximo:
    filtros_ativos.append(
        f"Valor máximo: {limite:.2f}"
    )
st.subheader("Visão geral")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric(
    label="Total da base",
    value=f"{total_base:,}".replace(",", ".")
)
c2.metric(
    label="Transações no resultado",
    value=f"{total_filtrado:,}".replace(",", ".")
)
c3.metric(
    label="Fraudes no resultado",
    value=f"{fraudes:,}".replace(",", ".")
)
c4.metric(
    label="Taxa de fraude",
    value=f"{taxa:.3f}%"
)
c5.metric(
    label="Valor das fraudes",
    value=f"{valor_fraudes:,.2f}"
)
if filtros_ativos:
    st.info(
        "Filtros aplicados: "
        + " | ".join(filtros_ativos)
        + f" | Transações encontradas: {total_filtrado:,}".replace(",", ".")
    )
else:
    st.caption(
        "Nenhum filtro está restringindo os dados."
        f"Exibindo {total_filtrado:,} transações.".replace(",", ".")
    )
if filtrado.empty:
    st.warning("Nenhuma transação corresponde aos filtros.")
    st.stop()

# Gráfico 1: distribuição das classes
st.header("1. Distribuição das Transações")
col1, col2 = st.columns(2)
with col1:
    contagem = (
        filtrado["Tipo"]
        .value_counts()
        .reindex(["Legítima", "Fraude"], fill_value=0)
    )
    fig, ax = plt.subplots(figsize=(7, 4))
    contagem.plot(kind="bar", ax=ax)
    ax.set_xlabel("Tipo")
    ax.set_ylabel("Transações")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# Gráfico 2: valores das transações
with col2:
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(
        data=filtrado,
        x="Tipo",
        y="Amount",
        ax=ax
    )
    ax.set_yscale("symlog")
    ax.set_title("Valores por tipo de transação")
    ax.set_xlabel("Tipo")
    ax.set_ylabel("Valor (escala symlog)")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# Gráfico 3: distribuição temporal
st.header("2. Distribuição Temporal")
fraudes_hora= (
    filtrado[filtrado["Class"] == 1]
    .groupby("Hora_aproximada")
    .size()
    .reindex(range(24), fill_value=0)
)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(fraudes_hora.index, fraudes_hora.values, marker="o")
ax.set_title("Fraude por hora aproximada")
ax.set_xlabel("Hora aproximada")
ax.set_ylabel("Quantidade")
ax.set_xticks(range(0, 24, 2))
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Gráfico 4: correlação
st.header("3. Correlação entre Variáveis")
colunas_corr = ["Time", "Amount"] + [
    f"V{i}" for i in range(1, 29)
] + ["Class"]
corr = filtrado[colunas_corr].corr()
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(
    corr,
    cmap="coolwarm",
    center=0,
    ax=ax
)
ax.set_title("Mapa de correlação")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Estatísticas para consulta
st.header("4. Resumo Estatístico")
st.dataframe(
    filtrado.groupby("Tipo")["Amount"].agg(
    contagem="count",
    média="mean",
    desvio_padrao="std",
    mínimo="min",
    máximo="max"
).round(2),
    use_container_width=True
)
