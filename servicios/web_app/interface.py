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
st.markdown('<p class="f1-title"> FI LIVE HUB: CONSULTA DE ESTADÍSTICA RT</p>', unsafe_allow_html=True)
busqueda = st.text_input("Buscar", placeholder="🔍 BUSCAR PILOTO, EQUIPO...", label_visibility="collapsed")
st.divider()


# --- CARGA DE DATOS ---
ruta_csv = "data/clean/drivers_list.csv"
ruta_points = "data/clean/archivo_2.csv"

if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)
    col_n = df.columns[0]
    
    # Cargar puntos de archivo_2.csv
    df_points = pd.read_csv(ruta_points)
    # Crear diccionario de puntos por nombre (normalizar para matching)
    puntos_dict = {}
    for idx, row in df_points.iterrows():
        # Normalizar nombres especiales
        nombre = row['nombre'].replace('Andrea Kimi', 'Kimi').strip()
        apellido = row['apellido'].replace('ü', 'u').upper()
        nombre_normalizado = f"{nombre.upper()} {apellido}"
        puntos_dict[nombre_normalizado] = row['puntos']
    
    # Agregar puntos al dataframe
    df['puntos'] = df[col_n].apply(lambda x: puntos_dict.get(x.upper(), 0))
    # Ordenar por puntos (descendente)
    df = df.sort_values('puntos', ascending=False).reset_index(drop=True) 

    # --- MOVER LA LISTA AQUÍ (Antes de usarla en t1) ---
    lista_fotos = [
        "https://img2.51gt3.com/rac/racer/202503/cfc139b2b49e48cd80a436c00a71711d.png", # Verstappen
        "https://img.redbull.com/images/c_crop,x_914,y_1637,h_3171,w_3171/c_fill,w_308,h_308/q_auto:low,f_auto/redbullcom/2022/5/5/esxtfazwc5k0xntwv20i/max-verstappen-profile-pic", # Norris
        "https://img2.51gt3.com/rac/racer/202503/4a3ecd96c2fd49508824cae497bfcec3.png?x-oss-process=style/_nowm", # Bortoleto 
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpOdpFWHKoK6ZLKyWG760LL0wIjfvVz9jkwQ&s", # Hadjar
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSosRLhYZ0ZrhSkCM9w97fkgDMrY7yF7Uy-g&s", # Jack Doohan (Alpine)
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9swwiCzY4ulkHmWcYjDC4JZm9d_n4G_zavQ&s", # Pierre Gasly (Alpine)
        "https://preview.redd.it/fun-fact-andrea-kimi-antonelli-might-be-the-first-f1-driver-v0-0uznvsuwu8ve1.jpeg?width=640&crop=smart&auto=webp&s=3c3ca7185c5a1f438fbbd051bd3b8c881abc4d06", # Kimi Antonelli (Mercedes)
        "https://img2.51gt3.com/rac/racer/202503/1f1fd439e5344c7a83faf4a80d09486f.png", # Fernando Alonso (Aston Martin) --
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMolyGxbEvjWbsApmtV5zJkofNtuZHxaxO-Q&s", # Charles Leclerc (Ferrari)
        "https://media.formula1.com/image/upload/f_auto,c_limit,q_75,w_1320/content/dam/fom-website/drivers/2024Drivers/alonso", # Lance Stroll (Aston Martin)
        "https://img2.51gt3.com/rac/racer/202503/737aac3065d74096b767308cf4c3164e.png?x-oss-process=style/_nhd_en", # Yuki Tsunoda (RB) Nico
        "https://img2.51gt3.com/rac/racer/202503/12a32c8783f24aec8fce1d35138941a7.png", # Alexander Albon (Williams)Isack hadjar 
        "https://img2.51gt3.com/rac/racer/202503/b4e1b56f7f2a4c989f16787b26852cba.png?x-oss-process=style/_nhd_en", # Nico Hulkenberg (Sauber) oliver 
        "https://img2.51gt3.com/rac/racer/202503/34d4155677ae4874aae0240f9b366cc3.png?x-oss-process=style/_nowm", # Liam Lawson (Red Bull) Esteban Ocon 
        "https://img2.51gt3.com/rac/racer/202503/3a6b5ab450b040feb7cab3cb50e9a53f.png?x-oss-process=style/_nowm", # Esteban Ocon (Haas)Liam Lawson
        "https://media.formula1.com/image/upload/f_auto,c_limit,q_75,w_1320/content/dam/fom-website/drivers/2025Drivers/tsunoda", # Lewis Hamilton (Ferrari) Yuki tsunoda
        "https://img2.51gt3.com/rac/racer/202503/2869081e10e6412894446d1320c9cb44.png?x-oss-process=style/_nowm", # Carlos Sainz (Williams) Lance stroll
        "https://media.formula1.com/image/upload/f_auto,c_limit,q_75,w_1320/content/dam/fom-website/drivers/2025Drivers/gasly", # George Russell (Mercedes)Pierra Gasly
        "https://www.grandprix.com.au/uploads/images/_driverProfile/394780/FOR-GP26-DRIVER_PROFILE-M-Gabriel_Bortoleto.webp", # Oscar Piastri (McLaren) Gabriel Bortoleto
        "https://static.wikia.nocookie.net/f1wikia/images/0/0f/Doohan2025.png/revision/latest?cb=20250728004628"  # Oliver Bearman (Haas)Jack DOohan
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
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/66/McLaren_Racing_logo.svg/3840px-McLaren_Racing_logo.svg.png" >
                <h3 style="margin:10px 0;">McLaren</h3>
            </div>
        ''', unsafe_allow_html=True)
    
    with t3:
        st.markdown(f"""
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold; font-size: 20px"> TOP 5 PILOTOS</p>
                <p style="text-align: center; padding-left: 9px; margin-top: 10px; font-size: 18.5px;font-weight: bold;">
                    1º: {df.iloc[0][col_n]}<br>
                    2º: {df.iloc[1][col_n]}<br>
                    3º: {df.iloc[2][col_n]}<br>
                    4º: {df.iloc[3][col_n]}<br>
                    5º: {df.iloc[4][col_n]}
                </p>
            </div>
        """, unsafe_allow_html=True)

    # CARRUSEL DE PILOTOS
    if 'carousel_index' not in st.session_state:
        st.session_state.carousel_index = 0
    
    max_display = 4
    total_pilotos = len(df)
    
    # Botones de navegación
    col_nav_left, col_nav_center, col_nav_right = st.columns([1, 3, 1])
    
    with col_nav_left:
        if st.button("◀ Anterior", key="prev_carousel"):
            st.session_state.carousel_index = max(0, st.session_state.carousel_index - max_display)
    
    with col_nav_center:
        pilotos_mostrados = min(max_display, total_pilotos - st.session_state.carousel_index)
        inicio = st.session_state.carousel_index + 1
        fin = st.session_state.carousel_index + pilotos_mostrados
        st.markdown(f"<p style='text-align: center; color: #e10600;'><b>Pilotos {inicio} - {fin} de {total_pilotos}</b></p>", unsafe_allow_html=True)
    
    with col_nav_right:
        if st.button("Siguiente ▶", key="next_carousel"):
            if st.session_state.carousel_index + max_display < total_pilotos:
                st.session_state.carousel_index += max_display
    
    # Mostrar tarjetas del carrusel
    m = st.columns(4)
    
    for i in range(min(max_display, total_pilotos - st.session_state.carousel_index)):
        idx = st.session_state.carousel_index + i
        nombre = df.iloc[idx][col_n]
        puntos = int(df.iloc[idx]['puntos'])
        foto_url = lista_fotos[idx] if idx < len(lista_fotos) else "https://www.formula1.com/etc/designs/fom-website/images/helmet-placeholder.png"
        
        with m[i]:
            st.markdown(f"""
                <div class="card">
                    <img src="{foto_url}" width="130" style="border-radius: 50%; border: 3px solid #e10600; margin-bottom: 10px; object-fit: cover; aspect-ratio: 1/1;">
                    <p style="font-size: 18px;"><b>{nombre}</b></p>
                    <p style="color:red; font-weight:bold;">{puntos} PTS</p>
                </div>
            """, unsafe_allow_html=True)

    # 5. BLOQUE INFERIOR
    st.divider()
    b1, b2 = st.columns([1, 2])
    with b1:
        st.subheader("ÚLTIMA CARRERA:")
        st.markdown("""
        <div style="background-color: rgba(6, 104, 201, 0.2); padding: 15px; border-radius: 8px; color: white;">
            <p style="font-size: 18px; font-weight: bold; margin: 0 0 10px 0;"><strong>GP DE ARABIA SAUDITA</strong></p>
            <p style="margin: 0 0 15px 0;">Circuito de Jeddah Corniche</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/be/Jeddah_Formula_E_Layout.png" style="width:91%; border-radius: 6px; margin-bottom: 10px;">
            <p style="font-size: 13px; margin: 0; line-height: 1.5;">
                <strong>Longitud:</strong> 6,174 km<br>
                <strong>Curvas:</strong> 27<br>
                <strong>Rectas Principales:</strong> 3 <br><br>
                <strong>Sector 1:</strong> Curvas 1-4<br>
                <strong>Sector 2:</strong> Curvas 5-22<br>
                <strong>Sector 3:</strong> Curvas 23-27
            </p>
        </div>
        """, unsafe_allow_html=True)
    with b2:
        st.subheader(" CLASIFICACIÓN DE ESCUDERÍAS:")
        # Agrupar por escudería y sumar puntos
        df_teams = df.groupby('Escuderia')['puntos'].sum().reset_index()
        df_teams.columns = ['Escudería', 'Puntos']
        df_teams = df_teams.sort_values('Puntos', ascending=False).reset_index(drop=True)
        
        # Filtrar por búsqueda si existe
        df_teams_mostrar = df_teams.copy()
        if busqueda:
            df_teams_mostrar = df_teams[df_teams['Escudería'].str.contains(busqueda, case=False)]
        
        st.dataframe(df_teams_mostrar, width='stretch')
    st.divider()
    w1 = st.columns(3)[0]
    with w1:
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
    # 6. APARTADO DE AYUDA AL CLIENTE
    st.divider()
    
    st.markdown('<p style="font-size: 24px; font-weight: bold; color: #e10600; margin-bottom: 20px;"> AYUDA AL CLIENTE</p>', unsafe_allow_html=True)
    
    # Creamos 3 columnas para organizar el soporte
    h1, h2, h3 = st.columns(3)
    
    with h1:
        st.markdown("""
            <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-top: 4px solid #e10600; min-height: 180px;">
                <p style="font-weight: bold; font-size: 18px; margin-bottom: 10px;"> Soporte Técnico</p>
                <p style="font-size: 14px; color: #cccccc;">¿Tienes problemas con la visualización de datos?</p>
                <p style="font-size: 15px;"><b>Email:</b> soporte@f1livehub.com</p>
                <p style="font-size: 15px;"><b>Horario:</b> L-V 09:00 - 18:00 CET</p>
            </div>
        """, unsafe_allow_html=True)
        
    with h2:
        st.markdown("""
            <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-top: 4px solid #e10600; min-height: 180px;">
                <p style="font-weight: bold; font-size: 18px; margin-bottom: 10px;"> Documentación</p>
                <p style="font-size: 14px; color: #cccccc;">Consulta nuestras bibliografías para determinar el origen de nuestros datos.</p>
                <a href="#" style="color: #e10600; text-decoration: none; font-weight: bold;">Ver Manual de Usuario →</a><br> 
                <a href="#" style="color: #e10600; text-decoration: none; font-weight: bold;">API Reference (Ergast) →</a><br>
            </div>
        """, unsafe_allow_html=True) # Tendré que quitar el apartado de manual de usuario y añadir las referencias de a API
        
    with h3:
        st.markdown("""
            <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-top: 4px solid #e10600; min-height: 180px;">
                <p style="font-weight: bold; font-size: 18px; margin-bottom: 10px;"> Legal</p>
                <p style="font-size: 14px; color: #cccccc;">Información sobre privacidad y términos de servicio.</p>
                <ul style="font-size: 13px; padding-left: 20px; margin-top: 5px;">
                    <li>La Página no recolecta información personal del usuario.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Footer final
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; padding: 20px; color: #555555; font-size: 12px;">
            <p>© 2026 F1 Live Hub - Este sitio no es oficial y no está asociado de ninguna manera con el grupo de empresas de Fórmula 1.</p>
        </div>
    """, unsafe_allow_html=True)
else:
   st.error(" Ejecuta download.py en T2")



