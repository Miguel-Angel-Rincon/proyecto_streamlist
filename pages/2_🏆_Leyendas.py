# pages/2_Leyendas.py
import streamlit as st

st.set_page_config(page_title="Leyendas del Baloncesto", layout="wide")

# ================================
# Estilos
# ================================
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #141e30, #243b55);
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }
        .page-title {
            font-size: 3rem;
            font-weight: 900;
            text-align: center;
            margin: 40px 0 20px 0;
            background: linear-gradient(45deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .legend-card {
            background: rgba(255,255,255,0.08);
            border-radius: 15px;
            padding: 20px;
            margin: 15px;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        }
        .legend-card img {
            border-radius: 12px;
            margin-bottom: 15px;
        }
        .legend-card h3 {
            color: #ffcc70;
            margin-bottom: 10px;
        }
        .legend-card p {
            font-size: 1rem;
            line-height: 1.6;
            text-align: justify;
        }
    </style>
""", unsafe_allow_html=True)

# ================================
# Título
# ================================
st.markdown('<div class="page-title">🌟 Leyendas en Acción</div>', unsafe_allow_html=True)
st.markdown("Aquí celebramos a las figuras que marcaron una era en el baloncesto. Sus logros, estilo de juego y carisma los convirtieron en íconos mundiales.")

# ================================
# Leyendas - Cards en filas
# ================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="legend-card">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgkIOySDm9zY-6DZ8Vwq1ZW5zR0pnlLaltDA&s" width="100%" />
        <h3>🏀 Michael Jordan</h3>
        <p>Considerado por muchos como el mejor jugador de todos los tiempos. Ganó 6 campeonatos con los Chicago Bulls y revolucionó la NBA con su talento y mentalidad competitiva.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="legend-card">
        <img src="https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/28C4/production/_128563401_gettyimages-1463993781.jpg.webp" width="100%" />
        <h3>👑 LeBron James</h3>
        <p>Una de las figuras más dominantes de la historia. Su combinación de fuerza, inteligencia y habilidad lo ha llevado a ser líder en múltiples equipos y a romper récords de anotación.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="legend-card">
        <img src="https://media.cnn.com/api/v1/images/stellar/prod/200127110655-kobe-bryant-4-profile-shot.jpg?q=w_3000,h_2010,x_0,y_0,c_fill" width="100%" />
        <h3>🐍 Kobe Bryant</h3>
        <p>Conocido como "Black Mamba", Kobe dejó una huella imborrable en la NBA con su ética de trabajo, 5 títulos con Los Ángeles Lakers y momentos inolvidables en la cancha.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="legend-card">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR--VR-ELvotUDGgaO3zW-PPQUyEA4ZvPLErw&s" width="100%" />
        <h3>⛹️ Kareem Abdul-Jabbar</h3>
        <p>El máximo anotador histórico durante décadas. Su famoso "skyhook" se convirtió en una jugada imposible de detener. Un líder tanto dentro como fuera de la cancha.</p>
    </div>
    """, unsafe_allow_html=True)

# ================================
# Extra: Magic Johnson
# ================================
st.markdown("""
<div class="legend-card">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7Nebgm2jX0-DA85gxe-RGMtjoU-yVCJZsHA&s" width="60%" />
    <h3>✨ Magic Johnson</h3>
    <p>Maestro de las asistencias y de la visión de juego. Condujo a los Lakers a múltiples campeonatos en los años 80 y revolucionó el rol del base con su altura y creatividad.</p>
</div>
""", unsafe_allow_html=True)
