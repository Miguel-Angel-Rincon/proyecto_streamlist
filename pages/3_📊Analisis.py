import streamlit as st
import pandas as pd
import plotly.express as px

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
# Menú de gráficos
# ================================
st.markdown('<div class="section-card"><h2>📊 Visualizaciones Interactivas</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🏀 Puntos Totales", "📈 Partidos Jugados", "🔎 Puntos vs Asistencias"])

with tab1:
    st.markdown("### 🏀 Puntos totales por jugador")
    fig1 = px.bar(df, x="Jugador", y="Puntos", color="Jugador",
                  text="Puntos", template="plotly_dark",
                  color_discrete_sequence=px.colors.sequential.Reds)
    fig1.update_traces(textposition="outside")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.markdown("### 📈 Partidos disputados por leyenda")
    fig2 = px.line(df, x="Jugador", y="Partidos", markers=True,
                   template="plotly_dark", line_shape="linear",
                   color_discrete_sequence=["#00c3ff"])
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.markdown("### 🔎 Relación entre puntos y asistencias")
    fig3 = px.scatter(df, x="Puntos", y="Asistencias", size="Rebotes",
                      color="Jugador", template="plotly_dark",
                      hover_name="Jugador", size_max=60)
    st.plotly_chart(fig3, use_container_width=True)

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
    - Cada jugador aporta una dimensión distinta: anotación, liderazgo, rebotes o visión de juego.
    </p>
</div>
""", unsafe_allow_html=True)
