# app.py

import streamlit as st

st.set_page_config(page_title="Baloncesto Pro", layout="wide")

# ====== Estilos globales ======
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f0f1d);
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            font-size: 4rem;
            font-weight: 900;
            text-align: center;
            margin: 40px 0 20px 0;
            background: linear-gradient(45deg, #ff8a00, #e52e71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .main-subtitle {
            font-size: 1.6rem;
            color: #cfcfcf;
            text-align: center;
            margin-bottom: 40px;
        }
        .info-card {
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            padding: 30px;
            margin: 40px auto;
            max-width: 950px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.7);
            text-align: justify;
            line-height: 1.6;
            color: #ddd;
        }
        .feature-box {
            background: rgba(255,255,255,0.07);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 40px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.7);
            transition: transform 0.3s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .feature-box:hover {
            transform: translateY(-8px);
        }
        .feature-box h3 {
            color: #ff8a00;
            text-align: center;
            margin-bottom: 20px;
        }
        .feature-box p {
            color: #ddd;
            text-align: justify;
            flex-grow: 1;
        }
    </style>
""", unsafe_allow_html=True)

# ====== Contenido ======
st.markdown('<div class="main-title">🏀 Baloncesto </div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Historia, reglas y análisis visual en un entorno moderno</div>', unsafe_allow_html=True)

# Imagen principal
st.image(
   "https://static.vecteezy.com/system/resources/thumbnails/028/124/014/small_2x/close-up-view-of-glowing-basketball-ball-on-wet-floor-and-3d-court-generative-ai-photo.jpg",
    caption="Partido nocturno con luces intensas",
    use_container_width=True
)

st.markdown("""
<div class="info-card">
    En este proyecto exploraremos el baloncesto desde varios ángulos:
    su origen histórico, las reglas que dan forma al juego, los jugadores que se volvieron leyendas,
    y un análisis de datos con visualizaciones que muestran los patrones, tendencias y emociones del deporte.
</div>
""", unsafe_allow_html=True)

# ====== Tarjetas con columnas ======
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>📜 Historia & Evolución</h3>
        <p>Viaja desde los primeros días del baloncesto en los gimnasios hasta su expansión global, 
        con imágenes que capturan esos hitos.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>⭐ Leyendas en acción</h3>
        <p>Conoce a los jugadores más icónicos, sus momentos memorables y el impacto que han tenido en el deporte.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h3>📊 Análisis & Visualización</h3>
        <p>Tablas y gráficos (barras, líneas, pastel...) que permiten ver el juego desde los números, 
        entender tendencias y comparar rendimiento.</p>
    </div>
    """, unsafe_allow_html=True)
