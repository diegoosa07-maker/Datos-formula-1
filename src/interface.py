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
logo_col, title_col = st.columns([0.15, 0.85])

with logo_col:
    st.image("C:\\Users\\Pacho Landin\\Downloads\\Gemini_Generated_Image_rytchdrytchdrytc-removebg-preview.png", width=180)

with title_col:
    st.markdown('<p class="f1-title"> F1 LIVE HUB: CONSULTA DE ESTADÍSTICA RT</p>', unsafe_allow_html=True)

busqueda = st.text_input("Buscar", placeholder="🔍 BUSCAR PILOTO, EQUIPO...", label_visibility="collapsed")
st.divider()


# --- CARGA DE DATOS ---
ruta_csv = "data/clean/drivers_list.csv"

if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)
    col_n = df.columns[0] 

    # --- MOVER LA LISTA AQUÍ (Antes de usarla en t1) ---
    lista_fotos = [
        "https://img.redbull.com/images/c_crop,x_914,y_1637,h_3171,w_3171/c_fill,w_308,h_308/q_auto:low,f_auto/redbullcom/2022/5/5/esxtfazwc5k0xntwv20i/max-verstappen-profile-pic",
        "https://img2.51gt3.com/rac/racer/202503/cfc139b2b49e48cd80a436c00a71711d.png",
        "https://www.grandprix.com.au/uploads/images/_driverProfile/394780/FOR-GP26-DRIVER_PROFILE-M-Gabriel_Bortoleto.webp",
        "https://img2.51gt3.com/rac/racer/202503/12a32c8783f24aec8fce1d35138941a7.png"
    ]

    # 3. BLOQUE SUPERIOR
    t1, t2, t3 = st.columns(3)
    col_vacia_izq, t1, t2, t3, col_vacia_der = st.columns([1, 3, 3, 3, 1])
    with t1:
        # Ahora sí, lista_fotos ya existe
        foto_lider = lista_fotos[0]
        st.markdown(f"""
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold; font-size: 20px">LÍDER CAMPEONATO</p>
                <img src="{foto_lider}" width="100" style="border-radius: 50%; border: 3px solid #e10600; margin: 10px 0; object-fit: cover; aspect-ratio: 1/1;">
                <h3>{df.iloc[0][col_n]}</h3>
            </div>
        """, unsafe_allow_html=True)
    
    with t2:
        # Metemos el nombre y la imagen dentro del mismo st.markdown para que hereden el estilo de la tarjeta
        st.markdown(f'''
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold;font-size: 20px">ESCUDERÍA LÍDER</p>
                <img src="https://img.redbull.com/images/c_limit,w_4000/e_trim:1:transparent/c_limit,w_190,h_190/bo_5px_solid_rgb:00000000/q_auto:best,f_auto/redbullcom/2022/2/10/nhzwcy8ouv8jonuxscfx/red-bull-racing-tenant-logo">
                <h3 style="margin:10px 0;">RedBull Racing</h3>
            </div>
        ''', unsafe_allow_html=True)
    
    with t3:
        st.markdown(f"""
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold; font-size: 20px"> TOP 5 PILOTOS</p>
                <p style="text-align: center; padding-left: 9px; margin-top: 10px; font-size: 16px;font-weight: bold;">
                    1. {df.iloc[0][col_n]}<br>
                    2. {df.iloc[1][col_n]}<br>
                    3. {df.iloc[2][col_n]}<br>
                    4. {df.iloc[3][col_n]}<br>
                    5. {df.iloc[4][col_n]}
                </p>
            </div>
        """, unsafe_allow_html=True)

    # 4. PILOTOS DESTACADOS (Aquí ya no hace falta definir lista_fotos otra vez)
    st.markdown("### PILOTOS DESTACADOS:")
    m = st.columns(4)
    
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
        st.subheader(" PRÓXIMA CARRERA:")
        st.markdown("""
        <div style="background-color: rgba(6, 104, 201, 0.2); padding: 15px; border-radius: 8px; color: white;">
            <p style="font-size: 18px; font-weight: bold; margin: 0 0 10px 0;"><strong>GP DE MIAMI</strong></p>
            <p style="margin: 0 0 15px 0;">Circuito de Miami</p>
            <img src="https://live-production.wcms.abc-cdn.net.au/80ad9122fd89085f00471568c43698d3?src" style="width:100%; border-radius: 6px; margin-bottom: 10px;">
            <p style="font-size: 13px; margin: 0; line-height: 1.5;">
                <strong>Longitud:</strong> 5,41 km<br>
                <strong>Curvas:</strong> 19<br>
                <strong>Rectas Principales:</strong> 3 (más de 320km/h)<br><br>
                <strong>Sector 1:</strong> Curvas 1-8<br>
                <strong>Sector 2:</strong> Curvas 9-16<br>
                <strong>Sector 3:</strong> Curvas 17-19
            </p>
        </div>
        """, unsafe_allow_html=True)
    with b2:
        st.subheader(" CLASIFICACIÓN DE ESCUDERÍAS:")
        df_mostrar = df.copy()
        if busqueda:
            df_mostrar = df[df.astype(str).apply(lambda x: x.str.contains(busqueda, case=False)).any(axis=1)]
        st.dataframe(df_mostrar.head(20), width='stretch')
else:
   st.error(" Ejecuta download.py en T2")