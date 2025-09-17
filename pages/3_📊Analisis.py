import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ================================
# Configuración inicial
# ================================
st.set_page_config(page_title="Análisis de Leyendas del Baloncesto", layout="wide")

# ================================
# Estilos personalizados
# ================================
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }
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
st.markdown("Exploramos las estadísticas de **5 leyendas de la NBA**: Michael Jordan, LeBron James, Kobe Bryant, Kareem Abdul-Jabbar y Magic Johnson.")

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
# Tabla de datos
# ================================
with st.container():
    st.markdown('<div class="section-card"><h2>📋 Tabla de estadísticas</h2>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ================================
# Menú de gráficos (mejorados con go)
# ================================
st.markdown('<div class="section-card"><h2>📊 Visualizaciones Interactivas</h2>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "🏀 Puntos Totales", 
    "📈 Partidos Jugados", 
    "🔎 Puntos vs Asistencias", 
    "🏆 Títulos Ganados"
])

with tab1:
    st.markdown("### 🏀 Puntos totales por jugador (Barras con degradado)")
    fig1 = go.Figure(data=[
        go.Bar(
            x=df["Jugador"],
            y=df["Puntos"],
            text=df["Puntos"],
            textposition="outside",
            marker=dict(
                color=df["Puntos"],
                colorscale="Reds",
                line=dict(color="black", width=1.5)
            )
        )
    ])
    fig1.update_layout(
        template="plotly_dark",
        title="Puntos Totales",
        xaxis_title="Jugador",
        yaxis_title="Puntos",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.markdown("### 📈 Partidos disputados por leyenda (Curva Suave)")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=df["Jugador"], y=df["Partidos"],
        mode="lines+markers+text",
        text=df["Partidos"],
        textposition="top center",
        line=dict(color="#00c3ff", width=4, shape="spline"),
        marker=dict(size=12, color="#ffcc70", line=dict(color="black", width=2))
    ))
    fig2.update_layout(
        template="plotly_dark",
        title="Partidos disputados",
        xaxis_title="Jugador",
        yaxis_title="Partidos",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.markdown("### 🔎 Relación entre puntos y asistencias (Bubble Chart)")
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=df["Puntos"], y=df["Asistencias"],
        mode="markers+text",
        text=df["Jugador"],
        textposition="top center",
        marker=dict(
            size=df["Rebotes"] / 400,  # Escala para burbujas
            color=df["Asistencias"],
            colorscale="Viridis",
            showscale=True,
            line=dict(color="white", width=2)
        )
    ))
    fig3.update_layout(
        template="plotly_dark",
        title="Puntos vs Asistencias (tamaño según rebotes)",
        xaxis_title="Puntos",
        yaxis_title="Asistencias",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig3, use_container_width=True)

with tab4:
    st.markdown("### 🏆 Comparación de títulos ganados")
    fig4 = go.Figure(data=[
        go.Bar(
            x=df["Jugador"],
            y=df["Títulos"],
            text=df["Títulos"],
            textposition="outside",
            marker=dict(
                color=df["Títulos"],
                colorscale="Blues",
                line=dict(color="black", width=1.5)
            )
        )
    ])
    fig4.update_layout(
        template="plotly_dark",
        title="Títulos de la NBA por jugador",
        xaxis_title="Jugador",
        yaxis_title="Títulos",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================================
# Conclusión
# ================================
st.markdown("""
<div class="section-card">
    <h2>📌 Conclusiones</h2>
    <p>
    - <b>LeBron James</b> lidera en puntos, asistencias y rebotes, mostrando su versatilidad.<br>
    - <b>Kareem Abdul-Jabbar</b> sigue siendo un referente histórico con su récord de puntos.<br>
    - <b>Michael Jordan</b> y <b>Kobe Bryant</b> se consolidan como los mejores anotadores.<br>
    - <b>Magic Johnson</b> destaca por su visión de juego, siendo el máximo asistidor.<br>
    - En títulos, Jordan y Kareem dominan con <b>6 campeonatos</b> cada uno, seguidos muy de cerca por Kobe y Magic.
    </p>
</div>
""", unsafe_allow_html=True)
