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

# === BARRA LATERAL ===
with st.sidebar:
    st.markdown('<p class="f1-title">🏁 MENÚ</p>', unsafe_allow_html=True)
    opcion = st.selectbox(
        "Selecciona una sección",
        ("Inicio", "Pilotos", "Equipos", "Carreras")
    )

# 2. CABECERA Y BUSCADOR (Igual a tu dibujo)
st.markdown('<p class="f1-title"> DATA HUB: CONSULTA DE ESTADÍSTICA RT</p>', unsafe_allow_html=True)
busqueda = st.text_input("Buscar", placeholder="🔍 BUSCAR PILOTO, EQUIPO...", label_visibility="collapsed")
st.divider()


# --- CARGA DE DATOS ---
ruta_csv = "data/clean/drivers_list.csv"

if os.path.exists(ruta_csv):
    df = pd.read_csv(ruta_csv)
    col_n = df.columns[0] 

    # --- LISTA DE FOTOS ---
    lista_fotos = [
        "https://img.redbull.com/images/c_crop,x_914,y_1637,h_3171,w_3171/c_fill,w_308,h_308/q_auto:low,f_auto/redbullcom/2022/5/5/esxtfazwc5k0xntwv20i/max-verstappen-profile-pic",
        "https://img2.51gt3.com/rac/racer/202503/cfc139b2b49e48cd80a436c00a71711d.png",
        "https://www.grandprix.com.au/uploads/images/_driverProfile/394780/FOR-GP26-DRIVER_PROFILE-M-Gabriel_Bortoleto.webp",
        "https://img2.51gt3.com/rac/racer/202503/12a32c8783f24aec8fce1d35138941a7.png"
    ]

    # === SECCIÓN: INICIO ===
    if opcion == "Inicio":
        # 3. BLOQUE SUPERIOR
        col_vacia_izq, t1, t2, t3, col_vacia_der = st.columns([1, 3, 3, 3, 1])
        with t1:
            foto_lider = lista_fotos[0]
            st.markdown(f"""
                <div class="card">
                    <p style="color:red; margin:0; font-weight:bold; font-size: 20px">LÍDER CAMPEONATO</p>
                    <img src="{foto_lider}" width="100" style="border-radius: 50%; border: 3px solid #e10600; margin: 10px 0; object-fit: cover; aspect-ratio: 1/1;">
                    <h3>{df.iloc[0][col_n]}</h3>
                </div>
            """, unsafe_allow_html=True)
        
        with t2:
            st.markdown(f'''
                <div class="card">
                    <p style="color:red; margin:0; font-weight:bold;font-size: 20px">ESCUDERÍA LÍDER</p>
                    <img src="https://img.redbull.com/images/c_limit,w_4000/e_trim:1:transparent/c_limit,w_175,h_175/bo_5px_solid_rgb:00000000/q_auto:best,f_auto/redbullcom/2022/2/10/nhzwcy8ouv8jonuxscfx/red-bull-racing-tenant-logo">
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
            foto_url = lista_fotos[idx] if idx < len(lista_fotos) else "https://www.formula1.com/etc/designs/fom-website/images/helmet-placeholder.png"
            
            with m[i]:
                st.markdown(f"""
                    <div class="card">
                        <img src="{foto_url}" width="130" style="border-radius: 50%; border: 3px solid #e10600; margin-bottom: 10px; object-fit: cover; aspect-ratio: 1/1;">
                        <p style="font-size: 18px;"><b>{nombre}</b></p>
                        <p style="color:red; font-weight:bold;">{210 - (idx*15)} PTS</p>
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
            st.subheader("CLASIFICACIÓN DE ESCUDERÍAS:")
            df_mostrar = df.copy()
            if 'busqueda' in locals() and busqueda:
                df_mostrar = df[df.astype(str).apply(lambda x: x.str.contains(busqueda, case=False)).any(axis=1)]
            
            if df_mostrar.empty:
                st.error(" Ejecuta download.py en T2")
            else:
                st.dataframe(df_mostrar.head(20), use_container_width=True)

    # === SECCIÓN PILOTOS CON DATOS REALES ===
    elif opcion == "Pilotos":
        import json
        import pandas as pd
        
        # Inicializar session_state
        if 'piloto_seleccionado' not in st.session_state:
            st.session_state.piloto_seleccionado = None
        
        # CARGAR DATOS DE JSON
        try:
            with open('data/raw/drivers_data.json', 'r') as f:
                drivers_data = json.load(f)
            
            # Mapeo de códigos de país a nombres
            country_map = {
                "NED": "Países Bajos",
                "GBR": "Reino Unido",
                "AUS": "Australia",
                "CAN": "Canadá",
                "MEX": "México",
                "BRA": "Brasil",
                "ARG": "Argentina",
                "USA": "Estados Unidos",
                "ITA": "Italia",
                "FRA": "Francia",
                "DEU": "Alemania",
                "ESP": "España",
                "SWE": "Suecia",
                "NOR": "Noruega",
                "DNK": "Dinamarca",
                "FIN": "Finlandia",
                "JPN": "Japón",
                "THA": "Tailandia",
                "CHN": "China",
                "IND": "India",
                "RUS": "Rusia",
                "UKR": "Ucrania",
                "ZAF": "Sudáfrica",
                "SGP": "Singapur",
            }
            
            # Cargar datos de 2025 con puntos actuales
            drivers_points_2025 = {}
            driver_country = {}
            
            # Leer drivers2023_data para obtener country_code
            with open('data/raw/drivers2023_data.json', 'r') as f:
                for line in f:
                    data = json.loads(line)
                    driver_num = data.get('driver_number')
                    driver_country[driver_num] = country_map.get(data.get('country_code'), data.get('country_code', 'N/A'))
            
            # Leer drivers_2024_data para puntos de 2025 (datos actuales)
            with open('data/raw/drivers_2024_data.json', 'r') as f:
                for line in f:
                    data = json.loads(line)
                    driver_num = data.get('driver_number')
                    # Guardar el máximo de points_current para cada piloto
                    current_points = data.get('points_current', 0)
                    if driver_num not in drivers_points_2025 or current_points > drivers_points_2025[driver_num]:
                        drivers_points_2025[driver_num] = current_points
        except FileNotFoundError as e:
            st.error(f" Error: {e}")
            drivers_data = []
            drivers_points_2025 = {}
            driver_country = {}
            country_map = {}
        
        # === VISTA INDIVIDUAL: PERFIL DEL PILOTO ===
        if st.session_state.piloto_seleccionado is not None:
            # Botón volver
            if st.button(" Volver a la parrilla"):
                st.session_state.piloto_seleccionado = None
                st.rerun()
            
            st.divider()
            
            # Buscar piloto en los datos
            piloto = next((p for p in drivers_data if p.get('full_name') == st.session_state.piloto_seleccionado), None)
            
            if piloto:
                # Datos de referencia: edad y altura de pilotos F1
                driver_info = {
                    "Max VERSTAPPEN": {"edad": 26, "altura": "180 cm"},
                    "Lando NORRIS": {"edad": 24, "altura": "170 cm"},
                    "Gabriel BORTOLETO": {"edad": 22, "altura": "183 cm"},
                    "Isack HADJAR": {"edad": 24, "altura": "185 cm"},
                    "Jack DOOHAN": {"edad": 21, "altura": "183 cm"},
                    "Pierre GASLY": {"edad": 28, "altura": "178 cm"},
                    "Kimi ANTONELLI": {"edad": 24, "altura": "185 cm"},
                    "Fernando ALONSO": {"edad": 42, "altura": "179 cm"},
                    "Charles LECLERC": {"edad": 26, "altura": "178 cm"},
                    "Lance STROLL": {"edad": 25, "altura": "185 cm"},
                    "Yuki TSUNODA": {"edad": 24, "altura": "164 cm"},
                    "Alexander ALBON": {"edad": 28, "altura": "177 cm"},
                    "Nico HULKENBERG": {"edad": 36, "altura": "182 cm"},
                    "Liam LAWSON": {"edad": 22, "altura": "180 cm"},
                    "Esteban OCON": {"edad": 28, "altura": "186 cm"},
                    "Lewis HAMILTON": {"edad": 39, "altura": "183 cm"},
                    "Carlos SAINZ": {"edad": 29, "altura": "183 cm"},
                    "George RUSSELL": {"edad": 26, "altura": "183 cm"},
                    "Oscar PIASTRI": {"edad": 23, "altura": "180 cm"},
                    "Oliver BEARMAN": {"edad": 22, "altura": "183 cm"},
                }
                
                # Escuderías pasadas de algunos pilotos
                past_teams = {
                    "Max VERSTAPPEN": ["Toro Rosso"],
                    "Lando NORRIS": ["McLaren"],
                    "Fernando ALONSO": ["Renault", "Alpine", "McLaren", "Aston Martin"],
                    "Lewis HAMILTON": ["McLaren", "Mercedes"],
                    "Carlos SAINZ": ["Toro Rosso", "McLaren", "Ferrari"],
                }
                
                # Nombre en grande
                st.markdown(f"<h1 style='text-align: center; color: #e10600;'>{piloto.get('full_name', 'N/A')}</h1>", unsafe_allow_html=True)
                
                # Foto del piloto
                col_foto_izq, col_foto, col_foto_der = st.columns([1, 2, 1])
                with col_foto:
                    try:
                        st.image(piloto.get('headshot_url', ''), width=250)
                    except:
                        st.info("Foto no disponible")
                
                st.divider()
                
                # === BLOQUE 1: DATOS DEL PILOTO ===
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.subheader(" Datos del Piloto")
                    full_name = piloto.get('full_name', 'N/A')
                    edad = driver_info.get(full_name, {}).get('edad', 'N/A')
                    altura = driver_info.get(full_name, {}).get('altura', 'N/A')
                    nacionalidad = driver_country.get(piloto.get('driver_number'), 'N/A')
                    
                    st.write(f"**Nombre:** {full_name}")
                    st.write(f"**Edad:** {edad} años")
                    st.write(f"**Altura:** {altura}")
                    st.write(f"**Nacionalidad:** {nacionalidad}")
                
                # === BLOQUE 2: DATOS DE EQUIPO ===
                with col2:
                    st.subheader("🏁 Equipo")
                    equipo_actual = piloto.get('team_name', 'N/A')
                    color = piloto.get('team_colour', 'FFFFFF')
                    
                    st.write(f"**Escudería Actual:**")
                    st.write(f"*{equipo_actual}*")
                    st.markdown(f"<div style='background-color: #{color}; width: 100px; height: 40px; border-radius: 5px; border: 2px solid #e10600;'></div>", unsafe_allow_html=True)
                    
                    st.write("")
                    st.write(f"**Escuderías Pasadas:**")
                    past = past_teams.get(full_name, [])
                    if past:
                        for team in past:
                            st.write(f"• {team}")
                    else:
                        st.write("_(Datos no disponibles)_")
                
                # === BLOQUE 3: RENDIMIENTO ===
                with col3:
                    st.subheader(" Rendimiento 2025")
                    puntos_actuales = drivers_points_2025.get(piloto.get('driver_number'), 0)
                    st.metric("Puntos 2025", f"{puntos_actuales:.0f}")
                
                st.divider()
                
                # === GRÁFICA DE EVOLUCIÓN DE PUNTOS 2025 ===
                st.subheader(" Evolución de Puntos - Temporada 2025")
                
                # Crear datos realistas simulando progresión de carreras 2025
                num_carreras = 24
                if puntos_actuales > 0:
                    puntos_por_carrera = puntos_actuales / num_carreras
                else:
                    puntos_por_carrera = 0
                
                datos_historico = pd.DataFrame({
                    'Carrera': [f'R{i+1}' for i in range(num_carreras)],
                    'Puntos Acumulados': [round(puntos_por_carrera * (i+1)) for i in range(num_carreras)]
                })
                
                st.line_chart(datos_historico.set_index('Carrera'), use_container_width=True)
            else:
                st.error(" Piloto no encontrado en la base de datos")
        
        # === VISTA GENERAL: PARRILLA DE PILOTOS ===
        else:
            st.subheader(" Parrilla de Pilotos")
            
            # Carrusel
            if 'carousel_index' not in st.session_state:
                st.session_state.carousel_index = 0
            
            max_display = 4
            total_pilotos = len(drivers_data)
            
            # Botones de navegación
            col_nav_left, col_nav_center, col_nav_right = st.columns([1, 3, 1])
            
            with col_nav_left:
                if st.button("◀ Anterior", key="prev_carousel_pilotos"):
                    st.session_state.carousel_index = max(0, st.session_state.carousel_index - max_display)
            
            with col_nav_center:
                pilotos_mostrados = min(max_display, total_pilotos - st.session_state.carousel_index)
                inicio = st.session_state.carousel_index + 1
                fin = st.session_state.carousel_index + pilotos_mostrados
                st.markdown(f"<p style='text-align: center; color: #e10600;'><b>Pilotos {inicio} - {fin} de {total_pilotos}</b></p>", unsafe_allow_html=True)
            
            with col_nav_right:
                if st.button("Siguiente ▶", key="next_carousel_pilotos"):
                    if st.session_state.carousel_index + max_display < total_pilotos:
                        st.session_state.carousel_index += max_display
            
            st.divider()
            
            # Mostrar tarjetas del carrusel
            m = st.columns(4)
            
            for i in range(min(max_display, total_pilotos - st.session_state.carousel_index)):
                idx = st.session_state.carousel_index + i
                piloto = drivers_data[idx]
                nombre = piloto.get('full_name', 'N/A')
                foto_url = piloto.get('headshot_url', 'https://www.formula1.com/etc/designs/fom-website/images/helmet-placeholder.png')
                driver_num = piloto.get('driver_number')
                puntos = drivers_points_2025.get(driver_num, 0)
                
                with m[i]:
                    st.markdown(f"""
                        <div class="card">
                            <img src="{foto_url}" width="130" style="border-radius: 50%; border: 3px solid #e10600; margin-bottom: 10px; object-fit: cover; aspect-ratio: 1/1;">
                            <p style="font-size: 18px;"><b>{nombre}</b></p>
                            <p style="color:red; font-weight:bold;">{puntos:.0f} PTS</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Botón " Ver Perfil"
                    if st.button(" Ver Perfil", key=f"ver_perfil_{idx}"):
                        st.session_state.piloto_seleccionado = nombre
                        st.rerun()

    # === SECCIÓN: EQUIPOS ===
    elif opcion == "Equipos":
        st.subheader(" Equipos de F1")
        st.write("Sección en desarrollo...")

    # === SECCIÓN: CARRERAS ===
    elif opcion == "Carreras":
        st.subheader(" Carreras")
        st.write("Sección en desarrollo...")

else:
    st.error(" Archivo de datos no encontrado. Ejecuta download.py")

            