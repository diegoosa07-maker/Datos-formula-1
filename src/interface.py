import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN
st.set_page_config(page_title="F1 Live Hub", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #15151e; color: white; }
    .stApp { background-color: #15151e; }
    .card {
        background-color: #2b2b2b;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #e10600;
        margin-bottom: 10px;
        text-align: center;
        min-height: 220px;
    }
    .f1-title { font-size: 30px; font-weight: bold; color: #e10600; text-align: center; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CABECERA Y BUSCADOR (Igual a tu dibujo)
st.markdown('<p class="f1-title">s DATA HUB: CONSULTA DE ESTADÍSTICA RT</p>', unsafe_allow_html=True)
busqueda = st.text_input("", placeholder="🔍 BUSCAR PILOTO, EQUIPO...")
st.divider()

# --- CARGA DE DATOS ---
ruta_csv = "data/clean/drivers_list.csv"

if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)
    col_n = df.columns[0] 

    # 3. BLOQUE SUPERIOR
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown(f'<div class="card"><p style="color:red; margin:0;"> LÍDER CAMPEONATO</p><h3>{df.iloc[0][col_n]}</h3></div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="card"><p style="color:red; margin:0;"> ÚLTIMA CARRERA</p><h3>GP DE JAPÓN</h3></div>', unsafe_allow_html=True)
    with t3:
        st.markdown(f'<div class="card"><p style="color:red; margin:0;"> TOP 3 PILOTOS</p><p>1. {df.iloc[0][col_n]}<br>2. {df.iloc[1][col_n]}<br>3. {df.iloc[2][col_n]}</p></div>', unsafe_allow_html=True)

    # 4. PILOTOS DESTACADOS (Fotos por posición para que no fallen)
    st.markdown("###  PILOTOS DESTACADOS")
    m = st.columns(4)
    
    lista_fotos = [
        "https://media.formula1.com/content/dam/fom-website/drivers/2024Drivers/norris.jpg",
        "https://media.formula1.com/content/dam/fom-website/drivers/2024Drivers/verstappen.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Gabriel_Bortoleto_2024.jpg/440px-Gabriel_Bortoleto_2024.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Isack_Hadjar_F2_Austria_2022_%28cropped%29.jpg/440px-Isack_Hadjar_F2_Austria_2022_%28cropped%29.jpg"
    ]

    for i in range(min(4, len(df))):
        nombre = df.iloc[i][col_n]
        foto_url = lista_fotos[i] if i < len(lista_fotos) else "https://www.formula1.com/etc/designs/fom-website/images/helmet-placeholder.png"
        
        with m[i]:
            st.markdown(f"""
                <div class="card">
                    <img src="{foto_url}" width="130" style="border-radius: 50%; border: 3px solid #e10600; margin-bottom: 10px; object-fit: cover; aspect-ratio: 1/1;">
                    <p style="font-size: 18px;"><b>{nombre}</b></p>
                    <p style="color:red; font-weight:bold;">{210 - (i*15)} PTS</p>
                </div>
            """, unsafe_allow_html=True)

    # 5. BLOQUE INFERIOR
    st.divider()
    b1, b2 = st.columns([1, 2])
    with b1:
        st.subheader(" PRÓXIMA CARRERA")
        st.info("**GP DE CHINA**\n\nCircuito de Shanghái")
    with b2:
        st.subheader(" CLASIFICACIÓN DE ESCUDERÍAS")
        df_mostrar = df.copy()
        if busqueda:
            df_mostrar = df[df.astype(str).apply(lambda x: x.str.contains(busqueda, case=False)).any(axis=1)]
        st.dataframe(df_mostrar.head(10), use_container_width=True)
else:
    st.error(" Ejecuta download.py en T2")