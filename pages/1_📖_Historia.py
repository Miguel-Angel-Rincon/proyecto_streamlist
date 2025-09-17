# pages/1_Historia.py

import streamlit as st

st.set_page_config(page_title="Historia del Baloncesto", layout="wide")

# ====== Estilos ======
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #e0e0e0;
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
            padding: 30px;
            margin: 30px auto;
            max-width: 1100px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.6);
        }
        .section-card h2 {
            color: #ffcc70;
            margin-bottom: 15px;
            text-align: center;
        }
        .section-card p {
            font-size: 1.1rem;
            line-height: 1.7;
            text-align: justify;
        }
    </style>
""", unsafe_allow_html=True)

# ====== Contenido ======
st.markdown('<div class="page-title">📜 Historia y Evolución del Baloncesto</div>', unsafe_allow_html=True)

# Sección 1 - Origen
st.markdown("""
<div class="section-card">
    <h2>🏀 Los Inicios (1891)</h2>
    <p>
    El baloncesto nació en 1891, cuando James Naismith, un profesor de educación física en Springfield, Massachusetts, 
    buscaba un deporte que pudiera practicarse bajo techo durante el invierno. Su idea fue colgar dos canastas de melocotones 
    en lo alto de un gimnasio y usar un balón de fútbol para jugar. Así nació un deporte que pronto conquistaría al mundo.
    </p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://pbs.twimg.com/media/Epy-jZ1VQAEgHt9.jpg:large",
    caption="James Naismith, creador del baloncesto (1891).",
    use_container_width=True
)

# Sección 2 - Expansión
st.markdown("""
<div class="section-card">
    <h2>🌍 Expansión Mundial</h2>
    <p>
    A inicios del siglo XX, el baloncesto ya se practicaba en varios países gracias a la YMCA. 
    En 1936 fue reconocido como deporte olímpico en Berlín, y desde entonces se ha convertido en uno de los deportes más populares del planeta. 
    La creación de la NBA en 1946 marcó un antes y un después en la profesionalización del juego.
    </p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://0901.static.prezi.com/preview/v2/2y36x7fdtdl4ywd6knhmeeg4sh6jc3sachvcdoaizecfr3dnitcq_3_0.png",
    caption="Primer torneo olímpico de baloncesto en Berlín 1936.",
    use_container_width=True
)

# Sección 3 - Evolución Moderna
st.markdown("""
<div class="section-card">
    <h2>⚡ El Baloncesto Moderno</h2>
    <p>
    Hoy el baloncesto es un espectáculo global, con jugadores que son íconos culturales y ligas profesionales en múltiples países. 
    La evolución de las reglas, el estilo de juego más dinámico y la influencia de superestrellas como Michael Jordan, Kobe Bryant o LeBron James 
    han llevado este deporte a otro nivel, combinando pasión, estrategia y espectáculo.
    </p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://www.mundodeportivo.com/files/og_thumbnail/uploads/2021/02/04/60e7050179ee1.jpeg",
    caption="El baloncesto moderno: velocidad, emoción y espectáculo.",
    use_container_width=True
)
