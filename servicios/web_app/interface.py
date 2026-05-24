# IMPORTANTE: Este código uso tanto python como HTML para mejorar la estética, el video tutorial de HTML lo tienes en whatsapp por si necesitas repasar
import streamlit as st
import pandas as pd
import os
import base64
import json

# 0. CONFIGURACIÓN DE LA PÁGINA Y TARJETAS:
# He añadido una serie de comentarios para que así podamos entender mejor lo que hacen estos fragmentos de código HTML, los podeís ver a la derecha
# y usarlos para guiaros en la creación de nuevas secciones
st.set_page_config(page_title="F1 Live Hub", layout="wide")
st.markdown("""
    <style>
    /* Cambia el color de fondo general de la app a negro F1 (#15151e) y texto blanco */
    .main { background-color: #15151e; color: white; }
    .stApp { background-color: #15151e; }
    
    /* NUEVA CLASE: Contenedor tipo rectángulo redondeado para el título principal */
    .title-card {
        background-color: #2b2b2b;        /* Mismo gris oscuro que las tarjetas de datos */
        padding: 10px 25px;                /* Espaciado interno (arriba/abajo e izquierda/derecha) */
        border-radius: 10px;               /* Bordes redondeados idénticos al resto de la web */
        border: 2px solid #e10600;         /* Borde completo exterior con el rojo oficial F1 */
        display: inline-block;             /* Ajusta el tamaño de la caja al tamaño del texto */
        margin-top: 10px;                  /* Separación con el margen superior de la página */
    }
    
    /* Ajustes específicos para el texto del título dentro del nuevo contenedor */
    .f1-title { 
        font-size: 28px; 
        font-weight: bold; 
        color: #ffffff;                    /* Cambiado a blanco para que resalte sobre el borde rojo */
        margin: 0;                         /* Elimina márgenes por defecto para centrar el texto en la caja */
        letter-spacing: 1px;               /* Un toque sutil de separación de letras estilo racing */
    }
    
    /* Clase personalizada para las tarjetas de información */
    .card {
        background-color: #2b2b2b;        /* Gris oscuro de contraste */
        padding: 15px;                     /* Espaciado interno */
        border-radius: 10px;               /* Bordes redondeados */
        border-left: 5px solid #e10600;    /* Detalle del borde rojo de F1 a la izquierda */
        margin-bottom: 10px;               /* Separación con elementos inferiores */
        text-align: center;                /* Centra textos e imágenes por defecto */
        min-height: 240px;                 /* Altura mínima para homogeneizar el carrusel */
    }
    
    /* Configuración del círculo rojo para las fotos de los pilotos */
    .driver-photo {
        border-radius: 50%;                /* Recorte circular perfecto (requiere aspecto 1:1) */
        border: 3px solid #e10600;         /* Aro de color rojo rodeando la foto */
        margin: 10px auto;                 /* Centra la imagen horizontalmente con márgenes */
        object-fit: cover;                 /* Evita que la imagen se deforme al reescalar */
        aspect-ratio: 1/1;                 /* Fuerza a que el ancho y el alto sean idénticos */
        display: block;                    /* Permite aplicar los márgenes automáticos */
    }

    /* EDICIÓN REALIZADA: Configuración optimizada para los logos de las escuderías */
    .team-logo {
        border-radius: 8px;                /* Bordes ligeramente suavizados, no un círculo drástico */
        border: 2px solid #e10600;         /* Borde rojo de F1 perimetral */
        background-color: #ffffff;         /* Fondo blanco para homogeneizar falsos transparencias y dar contraste */
        padding: 5px;                      /* Pequeño colchón interno para que el logo no toque el borde */
        margin: 10px auto;                 /* Centrado horizontal */
        object-fit: contain;               /* Escala y contiene el logo entero sin recortar texto */
        display: block;                    /* Permite centrar con márgenes automáticos */
        height: 90px;                      /* Altura fija controlada */
        width: 140px;                      /* Anchura fija óptima para formatos panorámicos corporativos */
    }
    </style>
    """, unsafe_allow_html=True)

# FUNCIONES IA: Estas funciones han sido creadas por la IA para facilitarnos el uso de imágenes locales en streamlit y evitando conflictos con HTML
# EDICIÓN REALIZADA: Se añade el parámetro 'tipo' para discriminar entre estilos CSS de pilotos ('driver') y escuderías ('team')
def obtener_img_html(ruta_o_url, width=120, tipo="driver"):
    clase_css = "team-logo" if tipo == "team" else "driver-photo"
    
    if ruta_o_url.startswith("http"):
        return f'<img src="{ruta_o_url}" width="{width}" class="{clase_css}">'
    if os.path.exists(ruta_o_url):
        with open(ruta_o_url, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f'<img src="data:image/png;base64,{encoded_string}" width="{width}" class="{clase_css}">'     
    placeholder = "https://www.formula1.com/etc/designs/fom-website/images/helmet-placeholder.png"
    return f'<img src="{placeholder}" width="{width}" class="{clase_css}">'

def obtener_ruta_foto(nombre_entidad):
    carpeta_pics = "data/pics/"
    nombre_archivo_base = os.path.join(carpeta_pics, nombre_entidad.strip())
    extensiones = ['.png', '.jpg', '.avif', '.webp', '.jpeg']
    for ext in extensiones:
        ruta_completa = f"{nombre_archivo_base}{ext}"
        if os.path.exists(ruta_completa):
            return ruta_completa  
    return "https://www.formula1.com/etc/designs/fom-website/images/helmet-placeholder.png"

# Diccionario de logos de equipos
TEAM_LOGOS = {
    "Alpine": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/BWT_Alpine_F1_Team_Logo.png/500px-BWT_Alpine_F1_Team_Logo.png",
    "Aston Martin": "https://upload.wikimedia.org/wikipedia/en/1/15/Aston_Martin_Aramco_2024_logo.png",
    "Ferrari": "https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Scuderia_Ferrari_HP_logo_24.svg/500px-Scuderia_Ferrari_HP_logo_24.svg.png",
    "McLaren": "data/pics/McLaren.png",
    "Haas F1 Team": "https://static.wikia.nocookie.net/logopedia/images/c/c3/HaasF1Team2016ver.jpg/revision/latest/scale-to-width-down/250?cb=20260322174034",
    "Kick Sauber": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Logo_sauber_2023.jpg/500px-Logo_sauber_2023.jpg",
    "Racing Bulls": "https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/VCARB_F1_logo.svg/500px-VCARB_F1_logo.svg.png",
    "Williams": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Atlassian_Williams_F1_Team_logo.svg/500px-Atlassian_Williams_F1_Team_logo.svg.png",
    "Red Bull Racing": "data/pics/Red Bull Racing.png"
}

def obtener_logo_equipo(nombre_equipo):
    """Obtiene el logo de un equipo desde el diccionario o retorna la ruta local"""
    return TEAM_LOGOS.get(nombre_equipo.strip(), f"data/pics/{nombre_equipo.strip()}.png")

# FUNCIONES PARA GESTIONAR DATOS DE ESCUDERÍAS Y PILOTOS:
def cargar_pilotos_por_escuderia(temporada):
    """Carga el JSON de pilotos y crea un diccionario escudería -> pilotos"""
    ruta_json = f"data/raw/info/pilotos{temporada}_info.json"
    pilotos_por_escuderia = {}
    
    if os.path.exists(ruta_json):
        with open(ruta_json, 'r', encoding='utf-8') as f:
            for linea in f:
                try:
                    piloto_data = json.loads(linea)
                    escuderia = piloto_data.get('team_name', '')
                    nombre_completo = piloto_data.get('full_name', '')
                    
                    if escuderia and nombre_completo:
                        if escuderia not in pilotos_por_escuderia:
                            pilotos_por_escuderia[escuderia] = {
                                'pilotos': [],
                                'color_equipo': piloto_data.get('team_colour', '')
                            }
                        pilotos_por_escuderia[escuderia]['pilotos'].append(nombre_completo)
                except json.JSONDecodeError:
                    continue
    
    return pilotos_por_escuderia

def obtener_puntos_escuderia(df_pilotos, pilotos_escuderia):
    """Calcula los puntos totales y retorna datos de pilotos con sus puntos"""
    pilotos_con_puntos = []
    puntos_totales = 0
    
    for nombre_piloto in pilotos_escuderia:
        piloto_en_df = df_pilotos[df_pilotos['Nombre'] == nombre_piloto]
        if not piloto_en_df.empty:
            puntos = int(piloto_en_df.iloc[0]['Puntos'])
            pilotos_con_puntos.append({
                'nombre': nombre_piloto,
                'puntos': puntos
            })
            puntos_totales += puntos
    
    return pilotos_con_puntos, puntos_totales


# 1. ESTRUCTURA PRINCIPAL: TÍTULO, LOGO, SELECTOR DE TEMPORADAS Y BARRA DE BUSQUEDA
col_logo, col_titulo, col_selector = st.columns([1, 7, 2])
with col_logo:
    ruta_logo = "data/pics/logo.png"
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, width=75) # Logo estático en la esquina izquierda
# 1.1 TÍTULO DE LA PÁGINA
with col_titulo:
    st.markdown("""
        <div class="title-card">
            <p class="f1-title">F1 LIVE HUB: CONSULTA DE ESTADÍSTICA RT</p>
        </div>
    """, unsafe_allow_html=True)
# 1.2 SELECTOR DE TEMPORADAS
with col_selector:
    # Despliega un menú de las temporadas disponibles.
    temporada = st.selectbox("TEMPORADA", ["2023", "2024", "2025"], index=2) # La variable temporada se usará con gran frecuencia para filtrar y cargar datos correspondientes a cada año
# 1.3 BARRA DE BUSQUEDA
busqueda = st.text_input("Buscar", placeholder="🔍 BUSCAR PILOTO, EQUIPO...", label_visibility="collapsed") # La barra de busqueda aún no es funcional
st.divider() # Línea divisora, es meramente decorativa, no tiene una función importante


# 2. SECCIÓN DE PODIUMS Y CARRUSEL DE PILOTOS
# 2.1 CARGA DE DATOS DESDE CSV:
ruta_drivers_csv = f"data/clean/driverspodium{temporada}.csv" # Cargamos los datos desde sus correspondientes csv, haciendo uso de la variable temporada
ruta_teams_csv = f"data/clean/teamspodium{temporada}.csv" #    para cargar el año seleccionado en el menú desplegable
calendario_path = "data/clean/calendario.csv"
# Esos tres archivos contienen el podio para los pilotos, las escuderías y el calendario de carreras

# 2.2 VERIFICACIÓN DE ARCHIVOS, PODIO Y CARRUSEL:
if os.path.exists(ruta_drivers_csv) and os.path.exists(ruta_teams_csv):
    df_pilotos = pd.read_csv(ruta_drivers_csv)
    df_escuderias = pd.read_csv(ruta_teams_csv)
    col_vacia_izq, t1, t2, t3, col_vacia_der = st.columns([1, 3, 3, 3, 1])
    
    # Configuración de la tarjeta para el lider del campeonato.
    with t1:
        nombre_lider = df_pilotos.iloc[0]["Nombre"] # Siempre mostrar el piloto que este en la primera posición del csv
        img_html = obtener_img_html(obtener_ruta_foto(nombre_lider), width=100, tipo="driver") # Usamos la función creada por IA para obtener la imagen del piloto
        st.markdown(f"""
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold; font-size: 20px">LÍDER CAMPEONATO ({temporada})</p>
                {img_html}
                <h3 style="margin:0;">{nombre_lider}</h3>
            </div>
        """, unsafe_allow_html=True)
    # Configuración de la tarjeta para la escudería líder del campeonato
    with t2:
        escuderia_lider = df_escuderias.iloc[0]["Escudería"] # Siempre mostrar la escudería que este en la primera posición del csv
        ruta_foto_escuderia = obtener_ruta_foto(escuderia_lider)
        # EDICIÓN REALIZADA: Se pasa tipo="team" para que use las nuevas dimensiones rectangulares y el fondo contenedor limpio
        img_escuderia_html = obtener_img_html(ruta_foto_escuderia, width=140, tipo="team")
        
        st.markdown(f'''
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold;font-size: 20px">ESCUDERÍA LÍDER ({temporada})</p>
                <div style="height: 110px; display: flex; align-items: center; justify-content: center; margin: 5px 0;">
                    {img_escuderia_html}
                </div>
                <h3 style="margin:5px 0 0 0;">{escuderia_lider}</h3>
            </div>
        ''', unsafe_allow_html=True)
    # Configuración de la tarjeta para el top 5 pilotos del campeonato
    with t3:
        top_5_html = "" 
        for idx in range(min(5, len(df_pilotos))): # Únicamente mostrará hasta el top 5 de pilotos e ira cambiando según la variable temporada
            top_5_html += f"{idx+1}º: {df_pilotos.iloc[idx]['Nombre']}<br>"
            
        st.markdown(f"""
            <div class="card">
                <p style="color:red; margin:0; font-weight:bold; font-size: 20px"> TOP 5 PILOTOS</p>
                <p style="text-align: center; padding-left: 9px; margin-top: 10px; font-size: 18.5px; font-weight: bold; line-height: 1.4;">
                    {top_5_html}
                </p>
            </div>
        """, unsafe_allow_html=True)

    # Configuración del carrusel
    if "carousel_index" not in st.session_state or st.session_state.get("ultima_temporada") != temporada: # Reiniciamos el carrusel al cambiar de temporada
        st.session_state.carousel_index = 0
        st.session_state.ultima_temporada = temporada
    max_display = 4 # Solamente hemos puesto 4 pilotos por fila pero se podrían añadir más, aunque puede que afecte a la estética de la página
    total_pilotos = len(df_pilotos) 
    col_nav_left, col_nav_center, col_nav_right = st.columns([1, 3, 1])
    
    # Navegación del carrusel mediante botones
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
    
    # El carrusel en sí
    m = st.columns(4)
    for i in range(min(max_display, total_pilotos - st.session_state.carousel_index)): 
        idx = st.session_state.carousel_index + i # Sumamos el índice del carrusel a la posición del piloto para mostrar el piloto correcto 
        nombre = df_pilotos.iloc[idx]["Nombre"] # El nombre del piloto va cambiando con la ayuda del índice del carrusel 
        puntos = int(df_pilotos.iloc[idx]["Puntos"]) # Lo mismo para los puntos
        img_html = obtener_img_html(obtener_ruta_foto(nombre), width=120, tipo="driver")
        with m[i]:
            st.markdown(f"""
                <div class="card">
                    {img_html}
                    <p style="font-size: 18px; margin-top:10px; margin-bottom: 5px;"><b>{nombre}</b></p>
                    <p style="color:red; font-weight:bold; margin-bottom:0;">{puntos} PTS</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.error(f"No se encontraron los archivos de datos para la temporada {temporada}.")

# 3. PÁGINA DE DETALLE DE ESCUDERÍAS:
st.divider()
st.markdown('<p style="font-size: 24px; font-weight: bold; color: #e10600; margin-bottom: 20px;"> DETALLE DE ESCUDERÍAS</p>', unsafe_allow_html=True)

# Cargar datos de pilotos por escudería
pilotos_por_escuderia = cargar_pilotos_por_escuderia(temporada)

# Selector de escudería
col_selector_equipo, col_vacio = st.columns([2, 3])
with col_selector_equipo:
    escuderias_disponibles = sorted(df_escuderias['Escudería'].tolist())
    escuderia_seleccionada = st.selectbox(
        "Selecciona una escudería",
        escuderias_disponibles,
        index=0,
        key=f"select_team_{temporada}"
    )

# Mostrar detalle de la escudería seleccionada
if escuderia_seleccionada and escuderia_seleccionada in pilotos_por_escuderia:
    datos_escuderia = pilotos_por_escuderia[escuderia_seleccionada]
    pilotos_con_puntos, puntos_totales = obtener_puntos_escuderia(
        df_pilotos, 
        datos_escuderia['pilotos']
    )
    
    # Información general de la escudería
    col_info_1, col_info_2 = st.columns(2)
    
    with col_info_1:
        color_hex = datos_escuderia['color_equipo'] if datos_escuderia['color_equipo'] else "2b2b2b"
        ruta_logo_team = obtener_logo_equipo(escuderia_seleccionada)
        img_logo_html = obtener_img_html(ruta_logo_team, width=140, tipo="team")
        st.markdown(f"""
            <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-left: 5px solid #{color_hex}; text-align: center; height: 240px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <p style="color: #{color_hex}; font-size: 18px; font-weight: bold; margin: 0 0 10px 0;">ESCUDERÍA</p>
                <h2 style="margin: 0; color: white; margin-bottom: 10px;">{escuderia_seleccionada}</h2>
                <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
                    {img_logo_html}
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col_info_2:
        st.markdown(f"""
            <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-left: 5px solid #e10600; text-align: center; height: 240px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <p style="color: #e10600; font-size: 18px; font-weight: bold; margin: 0 0 10px 0;">PUNTOS TOTALES</p>
                <h1 style="margin: 0; color: white; font-size: 48px;">{int(puntos_totales)}</h1>
            </div>
        """, unsafe_allow_html=True)
    
    # Detalle de pilotos
    st.subheader("👤 PILOTOS DEL EQUIPO")
    col_piloto_1, col_piloto_2 = st.columns(2)
    
    for idx, piloto_info in enumerate(pilotos_con_puntos):
        col_actual = col_piloto_1 if idx % 2 == 0 else col_piloto_2
        with col_actual:
            ruta_foto = obtener_ruta_foto(piloto_info['nombre'])
            img_html = obtener_img_html(ruta_foto, width=120, tipo="driver")
            
            st.markdown(f"""
                <div class="card">
                    {img_html}
                    <h3 style="margin-top: 10px; margin-bottom: 5px;">{piloto_info['nombre']}</h3>
                    <p style="color: #e10600; font-weight: bold; font-size: 20px; margin: 10px 0;">{int(piloto_info['puntos'])} PTS</p>
                </div>
            """, unsafe_allow_html=True)
    
elif escuderia_seleccionada:
    st.warning(f"No se encontró información sobre los pilotos de {escuderia_seleccionada}")

# 4. CIRCUITOS Y CALENDARIO DE CARRERAS:
st.divider()
b1, b2 = st.columns([1, 2])
# 3.1 CIRCUITO DE LA ÚLTIMA CARRERA: 
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
# 3.2 TABLA DE CLASIFICACIÓN DE ESCUDERÍAS:
with b2:
    st.subheader(f" CLASIFICACIÓN DE ESCUDERÍAS ({temporada}):")
    if os.path.exists(ruta_teams_csv):
        df_teams_mostrar = df_escuderias.copy()
        if busqueda:
            df_teams_mostrar = df_escuderias[df_escuderias['Escudería'].str.contains(busqueda, case=False)]
        st.dataframe(df_teams_mostrar, use_container_width=True, hide_index=True)

st.divider() # Otra línea divisora, una vez más, es meramente decorativa
w1, w2 = st.columns(2)
# 3.3 CIRCUITO DE LA PRÓXIMA CARRERA:
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
# 3.4 CALENDARIO DE CARRERAS:
with w2:
    st.subheader("CALENDARIO DE CARRERAS:")
    if os.path.exists(calendario_path):
        df_calendario = pd.read_csv(calendario_path)
        st.dataframe(df_calendario, use_container_width=True, hide_index=True, height=465)
    else:
        st.warning("Archivo calendario.csv no encontrado en data/clean/")

# 5. AYUDA AL CLIENTE, SOPORTE TÉCNICO Y DOCUMENTACIÓN:
st.divider()
st.markdown('<p style="font-size: 24px; font-weight: bold; color: #e10600; margin-bottom: 20px;"> AYUDA AL CLIENTE</p>', unsafe_allow_html=True)
h1, h2, h3 = st.columns(3)
# 6.1 SOPORTE TÉCNICO
with h1:
    st.markdown("""
        <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-top: 4px solid #e10600; min-height: 180px;">
            <p style="font-weight: bold; font-size: 18px; margin-bottom: 10px;"> Soporte Técnico</p>
            <p style="font-size: 14px; color: #cccccc;">¿Tienes problemas con la visualización de datos?</p>
            <p style="font-size: 15px;"><b>Email:</b> soporte@f1livehub.com</p>
            <p style="font-size: 15px;"><b>Horario:</b> L-V 09:00 - 18:00 CET</p>
        </div>
    """, unsafe_allow_html=True)
# 6.2 DOCUMENTACIÓN Y API
with h2:
    st.markdown("""
        <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-top: 4px solid #e10600; min-height: 180px;">
            <p style="font-weight: bold; font-size: 18px; margin-bottom: 10px;"> Documentación y API</p>
            <p style="font-size: 14px; color: #cccccc;">Consulta las referencias de datos del sistema.</p>
            <a href="https://ergast.com/mrd/" target="_blank" style="color: #e10600; text-decoration: none; font-weight: bold;">API Reference (Ergast Motor Racing Data) →</a><br>
        </div>
    """, unsafe_allow_html=True)
# 6.3 INFORMACIÓN LEGAL Y POLÍTICA DE PRIVCIDAD
with h3:
    st.markdown("""
        <div style="background-color: #2b2b2b; padding: 20px; border-radius: 10px; border-top: 4px solid #e10600; min-height: 180px;">
            <p style="font-weight: bold; font-size: 18px; margin-bottom: 10px;"> Legal</p>
            <p style="font-size: 14px; color: #cccccc;">Información sobre privacidad y términos de servicio.</p>
            <ul style="font-size: 13px; padding-left: 20px; margin-top: 5px;">
                <li>La página no recolecta ni procesa información personal del usuario.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
# 4.4 DISCLAIMER
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; color: #555555; font-size: 12px;">
        <p>© 2026 F1 Live Hub - Este sitio no es oficial y no está asociado de ninguna manera con el grupo de empresas de Fórmula 1.</p>
    </div>
""", unsafe_allow_html=True)