import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ================================
# Configuración inicial
# ================================
st.set_page_config(page_title="Análisis de Leyendas del Baloncesto", layout="wide")

# ================================
# Estilos personalizados
# ================================
st.markdown("""
    <style>
        .page-title {
            font-size: 3rem;
            font-weight: 900;
            text-align: center;
            margin: 40px 0 20px 0;
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .section-card {
            background: rgba(255,255,255,0.07);
            border-radius: 20px;
            padding: 25px;
            margin: 30px auto;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        .section-card h2 {
            color: #ffcc70;
            text-align: center;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# ================================
# Título principal
# ================================
st.markdown('<div class="page-title">📊 Análisis de Leyendas del Baloncesto</div>', unsafe_allow_html=True)

# ================================
# Datos
# ================================
data = {
    "Jugador": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Kareem Abdul-Jabbar", "Magic Johnson"],
    "Partidos": [1072, 1421, 1346, 1560, 906],
    "Puntos": [32292, 38852, 33643, 38387, 17707],
    "Asistencias": [5633, 10667, 6306, 5660, 10141],
    "Rebotes": [6672, 10700, 7047, 17440, 6559],
    "Títulos": [6, 4, 5, 6, 5],
}
df = pd.DataFrame(data)

# ================================
# Tabla
# ================================
with st.container():
    st.markdown('<div class="section-card"><h2>📋 Tabla de estadísticas</h2>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ================================
# Menú de gráficos
# ================================
st.markdown('<div class="section-card"><h2>📊 Visualizaciones</h2>', unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏀 Puntos Totales", 
    "📈 Partidos Jugados", 
    "🔎 Puntos vs Asistencias", 
    "🏆 Títulos Ganados",
    "🌐 Radar Comparativo"
])

plt.style.use("dark_background")

# ========== TAB 1 ==========
with tab1:
    st.markdown("### 🏀 Puntos totales por jugador")
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(df["Jugador"], df["Puntos"], color="tomato")
    ax.set_title("Comparación de puntos anotados", fontsize=16)
    ax.set_ylabel("Puntos")
    plt.xticks(rotation=15)

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 500, f"{yval:,}", 
                ha="center", va="bottom", fontsize=9, color="yellow")
    st.pyplot(fig)

# ========== TAB 2 ==========
with tab2:
    st.markdown("### 📈 Partidos disputados por leyenda")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df["Jugador"], df["Partidos"], marker="o", linewidth=3, color="cyan")
    ax.set_title("Número total de partidos jugados", fontsize=16)
    ax.set_ylabel("Partidos")
    plt.xticks(rotation=15)

    for i, val in enumerate(df["Partidos"]):
        ax.text(i, val + 30, str(val), ha="center", fontsize=9, color="yellow")
    st.pyplot(fig)

# ========== TAB 3 ==========
with tab3:
    st.markdown("### 🔎 Relación entre puntos y asistencias")
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(df["Puntos"], df["Asistencias"], 
                         s=df["Rebotes"]/2, c=df["Asistencias"], cmap="viridis", edgecolors="white")
    ax.set_title("Relación entre puntos, asistencias y rebotes", fontsize=16)
    ax.set_xlabel("Puntos")
    ax.set_ylabel("Asistencias")
    for i, txt in enumerate(df["Jugador"]):
        ax.annotate(txt, (df["Puntos"][i], df["Asistencias"][i]), fontsize=9, color="white")
    fig.colorbar(scatter, ax=ax, label="Asistencias")
    st.pyplot(fig)

# ========== TAB 4 ==========
with tab4:
    st.markdown("### 🏆 Comparación de títulos ganados")
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(df["Jugador"], df["Títulos"], color="royalblue")
    ax.set_title("Cantidad de títulos NBA ganados", fontsize=16)
    ax.set_ylabel("Títulos")
    plt.xticks(rotation=15)

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, str(yval), 
                ha="center", va="bottom", fontsize=9, color="yellow")
    st.pyplot(fig)

# ========== TAB 5 ==========
with tab5:
    st.markdown("### 🌐 Radar comparativo de estadísticas")
    categories = ["Partidos", "Puntos", "Asistencias", "Rebotes", "Títulos"]
    N = len(categories)

    values = df[categories].values
    max_vals = values.max(axis=0)  # normalizar
    norm_values = values / max_vals  

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    for i, row in df.iterrows():
        vals = norm_values[i].tolist()
        vals += vals[:1]
        ax.plot(angles, vals, linewidth=2, label=row["Jugador"])
        ax.fill(angles, vals, alpha=0.15)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Radar comparativo (valores normalizados)", size=15, pad=20)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)
