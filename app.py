import streamlit as st

st.set_page_config(page_title="Correlatividades - ISPI 9054", page_icon="📚", layout="wide")

st.title("📚 Validador de Correlatividades - ISPI Nº 9054")
st.markdown("### Profesorado de Educación Primaria")
st.write("Seleccioná el estado actual de tus materias para verificar automáticamente cuáles tenés habilitadas para cursar y rendir.")

materias = [
    # Primer Año (12)
    "Psicología y Educación", "Pedagogía", "Sociología de la Educación", 
    "Historia Argentina y Latinoamericana", "Movimiento y Cuerpo I", "Taller de Práctica I",
    "Comunicación y Expresión Oral y Escrita", "Resolución de Problemas y Creatividad", 
    "Ciencias Naturales para una Cultura Ciudadana", "Problemáticas de las Ciencias Sociales", 
    "Área Estético Expresiva I", "Problemáticas Contemporáneas de la Educación Primaria I",
    # Segundo Año (10)
    "Didáctica General", "Filosofía de la Educación", "Conocimiento y Educación", 
    "Movimiento y Cuerpo II", "Taller de Práctica II", "Matemática y su Didáctica I", 
    "Ciencias Naturales y su Didáctica I", "Ciencias Sociales y su Didáctica I", 
    "Lengua y su Didáctica", "Sujeto de la Educación Primaria", 
    # Tercer Año (12)
    "Tecnologías de la Información y de la Comunicación", 
    "Historia Social de la Educación y Política Educativa Argentina",
    "Taller de Práctica III", "Matemática y su Didáctica II", "Ciencias Naturales y su Didáctica II", 
    "Ciencias Sociales y su Didáctica II", "Literatura y su Didáctica", "Alfabetización Inicial", 
    "Área Estético Expresiva II", "Problemáticas Contemporáneas de la Educación Primaria II", 
    "Espacio de Definición Institucional I", "Espacio de Definición Institucional II", 
    # Cuarto Año (3)
    "Ética, Trabajo Docente, Derechos Humanos y Ciudadanía",
    "Taller de Práctica IV", "Sexualidad Humana y Educación"
]

if 'estados' not in st.session_state:
    st.session_state.estados = {m: "Pendiente" for m in materias}

def set_estado_lote(rango_materias, estado):
    for m in rango_materias:
        st.session_state.estados[m] = estado
        st.session_state[f"sel_{m}"] = estado

# Sidebar para control global
st.sidebar.header("Panel de Control")
if st.sidebar.button("Resetear todo a Pendiente", type="primary"):
    set_estado_lote(materias, "Pendiente")
    st.rerun()

st.sidebar.divider()
st.sidebar.markdown("**Acciones Rápidas por Año**")

st.sidebar.markdown("Primer Año")
col1, col2 = st.sidebar.columns(2)
if col1.button("Regular", key="1r"): set_estado_lote(materias[:12], "Regular"); st.rerun()
if col2.button("Aprobado", key="1a"): set_estado_lote(materias[:12], "Aprobada"); st.rerun()

st.sidebar.markdown("Segundo Año")
col3, col4 = st.sidebar.columns(2)
if col3.button("Regular", key="2r"): set_estado_lote(materias[12:22], "Regular"); st.rerun()
if col4.button("Aprobado", key="2a"): set_estado_lote(materias[12:22], "Aprobada"); st.rerun()

st.sidebar.markdown("Tercer Año")
col5, col6 = st.sidebar.columns(2)
if col5.button("Regular", key="3r"): set_estado_lote(materias[22:34], "Regular"); st.rerun()
if col6.button("Aprobado", key="3a"): set_estado_lote(materias[22:34], "Aprobada"); st.rerun()

st.sidebar.markdown("Cuarto Año")
col7, col8 = st.sidebar.columns(2)
if col7.button("Regular", key="4r"): set_estado_lote(materias[34:], "Regular"); st.rerun()
if col8.button("Aprobado", key="4a"): set_estado_lote(materias[34:], "Aprobada"); st.rerun()

def get_e(m): return st.session_state.estados.get(m, "Pendiente")
def reg(m): return get_e(m) in ["Regular", "Aprobada"]
def apr(m): return get_e(m) == "Aprobada"

def evaluar_materias(m):
    # Por defecto
    cursar = "Sin correlativas"
    rendir = "Sin correlativas"

    # --- PRIMER AÑO ---
    if m in materias[:12]:
        return cursar, rendir

    # --- SEGUNDO AÑO ---
    elif m == "Didáctica General":
        cursar = "Habilitada" if reg("Pedagogía") and reg("Psicología y Educación") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Pedagogía") and apr("Psicología y Educación") else "Faltan correlativas"
    elif m == "Movimiento y Cuerpo II":
        cursar = "Habilitada" if reg("Movimiento y Cuerpo I") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Movimiento y Cuerpo I") else "Faltan correlativas"
    elif m == "Matemática y su Didáctica I":
        cursar = "Habilitada" if reg("Resolución de Problemas y Creatividad") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Resolución de Problemas y Creatividad") else "Faltan correlativas"
    elif m == "Ciencias Naturales y su Didáctica I":
        cursar = "Habilitada" if reg("Ciencias Naturales para una Cultura Ciudadana") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Ciencias Naturales para una Cultura Ciudadana") else "Faltan correlativas"
    elif m == "Ciencias Sociales y su Didáctica I":
        cursar = "Habilitada" if reg("Problemáticas de las Ciencias Sociales") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Problemáticas de las Ciencias Sociales") else "Faltan correlativas"
    elif m == "Lengua y su Didáctica":
        cursar = "Habilitada" if reg("Comunicación y Expresión Oral y Escrita") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Comunicación y Expresión Oral y Escrita") else "Faltan correlativas"
    elif m == "Sujeto de la Educación Primaria":
        cursar = "Habilitada" if reg("Psicología y Educación") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Psicología y Educación") else "Faltan correlativas"
    elif m == "Taller de Práctica II":
        talleres_esp = sum([1 for x in ["Comunicación y Expresión Oral y Escrita", "Resolución de Problemas y Creatividad", 
                                       "Ciencias Naturales para una Cultura Ciudadana", "Problemáticas de las Ciencias Sociales", 
                                       "Área Estético Expresiva I", "Problemáticas Contemporáneas de la Educación Primaria I"] if apr(x)])
        cond_c = apr("Taller de Práctica I") and reg("Pedagogía") and reg("Psicología y Educación") and talleres_esp >= 3
        cursar = "Habilitada" if cond_c else "Faltan correlativas"
        rendir = "Sin correlativas"

    # --- TERCER AÑO ---
    elif m == "Historia Social de la Educación y Política Educativa Argentina":
        cursar = "Habilitada" if reg("Historia Argentina y Latinoamericana") and reg("Sociología de la Educación") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Historia Argentina y Latinoamericana") and apr("Sociología de la Educación") else "Faltan correlativas"
    elif m == "Literatura y su Didáctica" or m == "Alfabetización Inicial":
        cursar = "Habilitada" if reg("Lengua y su Didáctica") and reg("Didáctica General") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Lengua y su Didáctica") and apr("Didáctica General") else "Faltan correlativas"
    elif m == "Matemática y su Didáctica II":
        cursar = "Habilitada" if reg("Matemática y su Didáctica I") and reg("Didáctica General") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Matemática y su Didáctica I") and apr("Didáctica General") else "Faltan correlativas"
    elif m == "Ciencias Naturales y su Didáctica II":
        cursar = "Habilitada" if reg("Ciencias Naturales y su Didáctica I") and reg("Didáctica General") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Ciencias Naturales y su Didáctica I") and apr("Didáctica General") else "Faltan correlativas"
    elif m == "Ciencias Sociales y su Didáctica II":
        cursar = "Habilitada" if reg("Ciencias Sociales y su Didáctica I") and reg("Didáctica General") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Ciencias Sociales y su Didáctica I") and apr("Didáctica General") else "Faltan correlativas"
    elif m == "Área Estético Expresiva II":
        cursar = "Habilitada" if reg("Área Estético Expresiva I") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Área Estético Expresiva I") else "Faltan correlativas"
    elif m == "Problemáticas Contemporáneas de la Educación Primaria II":
        cursar = "Habilitada" if reg("Problemáticas Contemporáneas de la Educación Primaria I") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Problemáticas Contemporáneas de la Educación Primaria I") else "Faltan correlativas"
    elif m == "Taller de Práctica III":
        aprobadas_1ro = sum([1 for x in materias[:12] if apr(x)])
        cond_c = (aprobadas_1ro == 12 and apr("Taller de Práctica II") and
                  reg("Didáctica General") and reg("Matemática y su Didáctica I") and 
                  reg("Ciencias Sociales y su Didáctica I") and reg("Ciencias Naturales y su Didáctica I") and 
                  reg("Lengua y su Didáctica") and reg("Sujeto de la Educación Primaria") and reg("Conocimiento y Educación"))
        cursar = "Habilitada" if cond_c else "Faltan correlativas"
        rendir = "Sin correlativas"

    # --- CUARTO AÑO ---
    elif m == "Ética, Trabajo Docente, Derechos Humanos y Ciudadanía":
        cursar = "Habilitada" if reg("Filosofía de la Educación") and reg("Conocimiento y Educación") and reg("Historia Social de la Educación y Política Educativa Argentina") else "Faltan correlativas"
        rendir = "Habilitada" if apr("Filosofía de la Educación") and apr("Conocimiento y Educación") and apr("Historia Social de la Educación y Política Educativa Argentina") else "Faltan correlativas"
    elif m == "Taller de Práctica IV":
        aprobadas_2do = sum([1 for x in materias[12:22] if apr(x)])
        cond_c = (aprobadas_2do == 10 and apr("Taller de Práctica III") and apr("Área Estético Expresiva II") and
                  reg("Matemática y su Didáctica II") and reg("Ciencias Sociales y su Didáctica II") and 
                  reg("Ciencias Naturales y su Didáctica II") and reg("Literatura y su Didáctica") and 
                  reg("Alfabetización Inicial") and reg("Tecnologías de la Información y de la Comunicación") and 
                  reg("Problemáticas Contemporáneas de la Educación Primaria II"))
        cursar = "Habilitada" if cond_c else "Faltan correlativas"
        rendir = "Sin correlativas"

    return cursar, rendir

# --- INTERFAZ VISUAL ---
st.markdown("### Seleccioná tus materias:")
tab1, tab2, tab3, tab4 = st.tabs(["Primer Año", "Segundo Año", "Tercer Año", "Cuarto Año"])

def renderizar_materias(lista_materias):
    for m in lista_materias:
        col1, col2, col3 = st.columns([3, 2, 3])
        col1.write(f"**{m}**")
        st.session_state.estados[m] = col2.selectbox("Estado", ["Pendiente", "Regular", "Aprobada"], key=f"sel_{m}", index=["Pendiente", "Regular", "Aprobada"].index(get_e(m)), label_visibility="collapsed")
        c, r = evaluar_materias(m)
        
        # Colorear texto
        color_c = "green" if c in ["Habilitada", "Sin correlativas"] else "red"
        color_r = "green" if r in ["Habilitada", "Sin correlativas"] else "red"
        
        # Aplicamos el salto de línea <br> para evitar que el texto se mezcle en pantallas chicas
        col3.markdown(f"<div style='font-size:0.95em; line-height:1.5;'>Cursar: <strong style='color:{color_c}'>{c}</strong><br>Rendir: <strong style='color:{color_r}'>{r}</strong></div>", unsafe_allow_html=True)
        st.divider()

with tab1: renderizar_materias(materias[:12])
with tab2: renderizar_materias(materias[12:22])
with tab3: renderizar_materias(materias[22:34])
with tab4: renderizar_materias(materias[34:])
